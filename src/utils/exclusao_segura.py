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


def contar_dependentes(colecao: str, id_documento: int) -> dict[str, int]:
    """Retorna {colecao_filha: quantidade} das coleções filhas que referenciam id_documento."""
    # TODO (Membro 3 - Bruno): Implementar contagem no MongoDB usando count_documents
    raise NotImplementedError("TODO (Membro 3 - Bruno): Implementar contar_dependentes no MongoDB.")


def excluir_com_dependentes(colecao: str, id_documento: int) -> dict[str, int]:
    """Remove recursivamente os documentos filhos/netos e por último o documento pai."""
    # TODO (Membro 3 - Bruno): Implementar exclusão recursiva em cascata no MongoDB
    raise NotImplementedError("TODO (Membro 3 - Bruno): Implementar excluir_com_dependentes no MongoDB.")


def excluir_registro_seguro(
    colecao: str, id_documento: int, descricao: str = "o documento"
) -> bool:
    """Fluxo completo de exclusão com confirmação e trava de integridade referencial."""
    # TODO (Membro 3 - Bruno): Implementar fluxo completo do item 7.c.5.i do edital
    print(f"[TODO - Membro 3 (Bruno)] Implementar excluir_registro_seguro para {colecao} ({id_documento}).")
    return False
