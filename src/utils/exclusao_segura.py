"""Padrão de exclusão segura no MongoDB (item 7.c.5.i do edital da C3).

Responsável: Membro 3 (Bruno Mauro Bayer Laiber)

Toda controladora deve excluir documentos através deste módulo, garantindo:
1. Confirmação com o usuário se deseja realmente remover o documento;
2. Verificação de documentos dependentes referenciados em outras coleções;
3. Caso possua dependentes, exibe a quantidade por coleção filha e pergunta
   se o usuário deseja remover os documentos das coleções filhas em cascata;
4. Executa a exclusão recursiva (`delete_many` / `delete_one`) no MongoDB.
"""

from __future__ import annotations

from conexion.mongo_queries import MongoQueries

# Chave principal (PK lógica) de cada coleção do modelo
CHAVES_PRIMARIAS = {
    "cursos": "id_curso",
    "alunos": "matricula",
    "categorias_atividade": "id_categoria",
    "administradores": "id_admin",
    "tickets_atividades": "id_ticket",
}

# Para cada coleção pai: (coleção filha, [campos FK que apontam para o pai])
DEPENDENCIAS = {
    "cursos": [
        ("alunos", ["id_curso"]),
    ],
    "alunos": [
        ("tickets_atividades", ["matricula_aluno"]),
    ],
    "categorias_atividade": [
        ("tickets_atividades", ["id_categoria"]),
    ],
    "administradores": [
        ("tickets_atividades", ["id_admin_avaliador"]),
    ],
    "tickets_atividades": [],
}

NOMES_AMIGAVEIS = {
    "cursos": "Cursos",
    "alunos": "Alunos",
    "categorias_atividade": "Categorias de Atividade",
    "administradores": "Administradores",
    "tickets_atividades": "Tickets de Atividades",
}


def _planejar_dependentes(db, colecao: str, ids: list) -> dict[str, set]:
    """Identifica os documentos afetados na ordem em que devem ser removidos."""
    plano = {}
    for filha, campos in DEPENDENCIAS[colecao]:
        filtros = [{campo: {"$in": ids}} for campo in campos]
        filtro = filtros[0] if len(filtros) == 1 else {"$or": filtros}
        chave_filha = CHAVES_PRIMARIAS[filha]
        documentos = list(db[filha].find(filtro, {"_id": 1, chave_filha: 1}))
        if not documentos:
            continue

        ids_filhos = [doc[chave_filha] for doc in documentos]
        plano.update(_planejar_dependentes(db, filha, ids_filhos))
        plano[filha] = {doc["_id"] for doc in documentos}
    return plano


def _contar_plano(db, plano: dict[str, set]) -> dict[str, int]:
    return {
        colecao: db[colecao].count_documents({"_id": {"$in": list(ids)}})
        for colecao, ids in reversed(plano.items())
    }


def contar_dependentes(colecao: str, id_documento: int) -> dict[str, int]:
    """Conta os documentos filhos e netos, por coleção."""
    mongo = MongoQueries()
    try:
        mongo.connect()
        plano = _planejar_dependentes(mongo.db, colecao, [id_documento])
        return _contar_plano(mongo.db, plano)
    finally:
        mongo.close()


def _executar_exclusao(db, colecao: str, id_mongo, plano: dict[str, set]) -> dict[str, int]:
    removidos = {}
    for filha, ids in plano.items():
        resultado = db[filha].delete_many({"_id": {"$in": list(ids)}})
        removidos[filha] = resultado.deleted_count
    removidos[colecao] = db[colecao].delete_one({"_id": id_mongo}).deleted_count
    return removidos


def excluir_com_dependentes(colecao: str, id_documento: int) -> dict[str, int]:
    """Remove os dependentes e o registro principal após a autorização do chamador."""
    mongo = MongoQueries()
    try:
        mongo.connect()
        db = mongo.db
        documento = db[colecao].find_one({CHAVES_PRIMARIAS[colecao]: id_documento})
        if documento is None:
            return {colecao: 0}
        plano = _planejar_dependentes(db, colecao, [id_documento])
        return _executar_exclusao(db, colecao, documento["_id"], plano)
    finally:
        mongo.close()


def excluir_registro_seguro(
    colecao: str, id_documento: int, descricao: str = "o documento"
) -> bool:
    """Confirma a remoção e solicita autorização específica para a cascata."""
    resposta = input(f"Confirma a exclusão de {descricao}? (S/N): ").strip().upper()
    if resposta not in {"S", "SIM"}:
        print("Exclusão cancelada.")
        return False

    mongo = MongoQueries()
    try:
        mongo.connect()
        db = mongo.db
        filtro = {CHAVES_PRIMARIAS[colecao]: id_documento}
        documento = db[colecao].find_one(filtro)
        if documento is None:
            print("O documento informado não existe.")
            return False

        plano = _planejar_dependentes(db, colecao, [id_documento])
        if plano:
            print("Este documento possui registros dependentes.")
            for filha, quantidade in _contar_plano(db, plano).items():
                print(f"- {NOMES_AMIGAVEIS[filha]}: {quantidade}")
            resposta = input("Excluir também os registros dependentes? (S/N): ")
            if resposta.strip().upper() not in {"S", "SIM"}:
                print("Exclusão cancelada. Os registros foram preservados.")
                return False

        if (
            db[colecao].find_one({**filtro, "_id": documento["_id"]}) is None
            or _planejar_dependentes(db, colecao, [id_documento]) != plano
        ):
            print("Os registros mudaram. Consulte a lista e faça uma nova tentativa.")
            return False

        removidos = _executar_exclusao(db, colecao, documento["_id"], plano)
        if not removidos[colecao]:
            print("O documento informado não existe mais.")
            return False

        print("Documento excluído com sucesso.")
        if plano:
            print(f"Documentos dependentes removidos: {sum(removidos.values()) - 1}.")
        return True
    finally:
        mongo.close()
