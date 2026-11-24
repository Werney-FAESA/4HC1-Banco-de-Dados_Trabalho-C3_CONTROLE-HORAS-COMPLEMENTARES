"""Script de criação das coleções e carga inicial no MongoDB (Item 5 do Edital C3).

Responsável: Membro 1 (Kaike Vaccari do Nascimento)

Execução:
    python3 src/createCollectionsAndData.py
"""

import logging
from conexion.mongo_queries import MongoQueries

LIST_OF_COLLECTIONS = [
    "cursos",
    "alunos",
    "categorias_atividade",
    "administradores",
    "tickets_atividades",
]

logger = logging.getLogger(name="Controle_Horas_Complementares_MongoDB")
logger.setLevel(level=logging.WARNING)
mongo = MongoQueries()

# Dados iniciais migrados do projeto ControleHorasComplementares (usuarios.csv e tickets.csv)
DADOS_INICIAIS = {
    "cursos": [
        {
            "id_curso": 1,
            "nome_curso": "Ciencia da Computacao",
            "horas_exigidas": 120,
            "coordenador": "Prof. M.Sc. Howard Roatti",
        },
        {
            "id_curso": 2,
            "nome_curso": "Sistemas de Informacao",
            "horas_exigidas": 100,
            "coordenador": "Prof. M.Sc. Howard Roatti",
        },
        {
            "id_curso": 3,
            "nome_curso": "Engenharia de Computacao",
            "horas_exigidas": 140,
            "coordenador": "Prof. M.Sc. Howard Roatti",
        },
    ],
    "alunos": [
        {
            "matricula": 202601,
            "nome_aluno": "Werney Ferreira Rocha",
            "email": "werney@faesa.br",
            "periodo": 4,
            "id_curso": 1,
        },
        {
            "matricula": 202602,
            "nome_aluno": "Daniel Lima Del'Antonio",
            "email": "daniel@faesa.br",
            "periodo": 4,
            "id_curso": 2,
        },
        {
            "matricula": 202603,
            "nome_aluno": "Kaike Vaccari do Nascimento",
            "email": "kaike@faesa.br",
            "periodo": 4,
            "id_curso": 1,
        },
        {
            "matricula": 202604,
            "nome_aluno": "Bruno Mauro Bayer Laiber",
            "email": "bruno@faesa.br",
            "periodo": 4,
            "id_curso": 1,
        },
        {
            "matricula": 202605,
            "nome_aluno": "Issacar Mattos Gutler",
            "email": "issacar@faesa.br",
            "periodo": 4,
            "id_curso": 2,
        },
        {
            "matricula": 202606,
            "nome_aluno": "Gabriel Antonio Galdino dos Santos",
            "email": "gabriel@faesa.br",
            "periodo": 4,
            "id_curso": 3,
        },
    ],
    "categorias_atividade": [
        {
            "id_categoria": 1,
            "nome_categoria": "CURSO",
            "limite_maximo_horas": 40,
            "descricao": "Cursos livres, bootcamps e certificacoes tecnicas",
        },
        {
            "id_categoria": 2,
            "nome_categoria": "EVENTO",
            "limite_maximo_horas": 15,
            "descricao": "Palestras, congressos, seminarios e semanas academicas",
        },
        {
            "id_categoria": 3,
            "nome_categoria": "PESQUISA",
            "limite_maximo_horas": 60,
            "descricao": "Iniciacao cientifica, artigos publicados e projetos de extensao",
        },
    ],
    "administradores": [
        {
            "id_admin": 9001,
            "nome_admin": "Coordenador FAESA",
            "email": "admin@faesa.br",
            "cargo": "Coordenador de Curso",
        },
        {
            "id_admin": 9002,
            "nome_admin": "Secretaria Academica FAESA",
            "email": "secretaria@faesa.br",
            "cargo": "Analista Academico",
        },
    ],
    "tickets_atividades": [
        {
            "id_ticket": 1,
            "matricula_aluno": 202601,
            "id_categoria": 1,
            "id_admin_avaliador": 9001,
            "titulo": "Curso de Java POO",
            "horas_solicitadas": 20,
            "horas_validadas": 20,
            "status": "APROVADO",
            "observacao_admin": "Certificado validado",
        },
        {
            "id_ticket": 2,
            "matricula_aluno": 202601,
            "id_categoria": 2,
            "id_admin_avaliador": 9001,
            "titulo": "Semana de Tecnologia FAESA",
            "horas_solicitadas": 15,
            "horas_validadas": 15,
            "status": "APROVADO",
            "observacao_admin": "Aprovado",
        },
        {
            "id_ticket": 3,
            "matricula_aluno": 202601,
            "id_categoria": 3,
            "id_admin_avaliador": 9001,
            "titulo": "Iniciacao Cientifica IA",
            "horas_solicitadas": 30,
            "horas_validadas": 0,
            "status": "RECUSADO",
            "observacao_admin": "Faltou assinatura do orientador",
        },
        {
            "id_ticket": 4,
            "matricula_aluno": 202602,
            "id_categoria": 1,
            "id_admin_avaliador": 9002,
            "titulo": "Curso de Banco de Dados MongoDB",
            "horas_solicitadas": 25,
            "horas_validadas": 25,
            "status": "APROVADO",
            "observacao_admin": "Certificado validado",
        },
        {
            "id_ticket": 5,
            "matricula_aluno": 202603,
            "id_categoria": 1,
            "id_admin_avaliador": 9001,
            "titulo": "Curso de Programacao Python",
            "horas_solicitadas": 30,
            "horas_validadas": 30,
            "status": "APROVADO",
            "observacao_admin": "Aceito",
        },
        {
            "id_ticket": 6,
            "matricula_aluno": 202603,
            "id_categoria": 2,
            "id_admin_avaliador": 9002,
            "titulo": "Palestra de Seguranca da Informacao",
            "horas_solicitadas": 5,
            "horas_validadas": 5,
            "status": "APROVADO",
            "observacao_admin": "Aprovado",
        },
        {
            "id_ticket": 7,
            "matricula_aluno": 202604,
            "id_categoria": 3,
            "id_admin_avaliador": None,
            "titulo": "Projeto de Extensao Comunitaria",
            "horas_solicitadas": 40,
            "horas_validadas": 0,
            "status": "PENDENTE",
            "observacao_admin": "Aguardando analise",
        },
    ],
}


def createCollections(drop_if_exists: bool = False):
    """Lista as coleções existentes e cria (ou recria) as 5 coleções do sistema."""
    mongo.connect()
    existing_collections = mongo.db.list_collection_names()
    for collection in LIST_OF_COLLECTIONS:
        if collection in existing_collections:
            if drop_if_exists:
                mongo.db.drop_collection(collection)
                logger.warning(f"{collection} dropped!")
                mongo.db.create_collection(collection)
                logger.warning(f"{collection} created!")
        else:
            mongo.db.create_collection(collection)
            logger.warning(f"{collection} created!")
    mongo.close()


def insert_many(data: list[dict], collection: str):
    if not data:
        return
    mongo.connect()
    mongo.db[collection].insert_many(data)
    mongo.close()


def seed_initial_data():
    for collection in LIST_OF_COLLECTIONS:
        registros = [ dict(item) for item in DADOS_INICIAIS.get(collection, []) ]
        insert_many(data=registros, collection=collection)
        logger.warning(f"{len(registros)} documents generated at {collection} collection")


if __name__ == "__main__":
    logging.warning("Starting MongoDB collection creation and seed...")
    createCollections(drop_if_exists=True)
    seed_initial_data()
    logging.warning("End")
