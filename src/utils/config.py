MENU_PRINCIPAL = """Menu Principal:
1 - Relatórios
2 - Inserir Documentos
3 - Atualizar Documentos
4 - Remover Documentos
5 - Sair
"""

MENU_RELATORIOS = """Menu Relatórios
1 - Relatório de Horas por Aluno (Sumarização / $group)
2 - Relatório de Tickets por Categoria (Sumarização / $group)
3 - Relatório de Tickets por Status (Sumarização / $group)
4 - Relatório Detalhado de Tickets, Alunos e Cursos (Junção / $lookup)
5 - Relatório de Alunos e seus Cursos (Junção / $lookup)
6 - Relatório de Cursos Cadastrados
7 - Relatório de Categorias de Atividade
8 - Relatório de Administradores
0 - Voltar ao menu principal
"""

MENU_ENTIDADES = """Entidades (Coleções)
1 - Cursos
2 - Alunos
3 - Categorias de Atividade
4 - Administradores
5 - Tickets de Atividades Complementares
"""


def query_count(collection_name: str):
    from conexion.mongo_queries import MongoQueries
    import pandas as pd

    mongo = MongoQueries()
    mongo.connect()

    my_collection = mongo.db[collection_name]
    total_documentos = my_collection.count_documents({})
    mongo.close()
    df = pd.DataFrame({f"total_{collection_name}": [total_documentos]})
    return df


def clear_console(wait_time: int = 3):
    import os
    from time import sleep

    sleep(wait_time)
    os.system("cls" if os.name == "nt" else "clear")
