"""Módulo de Relatórios do Sistema utilizando Aggregation Pipeline do MongoDB.

Responsável: Membro 4 (Daniel Lima Del'Antonio)

Requisitos obrigatórios do Edital C3 (Item 7.a.1 - 1,5 pontos):
- (i) Consultas realizando a sumarização / agrupamento (``$group``) de coleções (1,0 pt);
- (ii) Consultas realizando a junção de coleções (``$lookup``) (0,5 pt).
"""

from __future__ import annotations

import pandas as pd
from pymongo import ASCENDING

from conexion.mongo_queries import MongoQueries


class Relatorio:
    @staticmethod
    def _exibir_resultados(titulo: str, resultados: list[dict]) -> None:
        print(f"\n=== {titulo} ===")
        if resultados:
            print(pd.DataFrame(resultados).to_string(index=False))
        else:
            print("Nenhum registro encontrado.")
        input("Pressione Enter para sair do relatório...")

    # ------------------------------------------------------------------
    # Relatórios de Sumarização / Agrupamento ($group - Item 7.a.1.i)
    # ------------------------------------------------------------------

    def get_relatorio_horas_por_aluno(self):
        """Resume as horas de tickets por aluno e compara com a carga do curso."""
        pipeline = [
            {
                "$group": {
                    "_id": "$matricula_aluno",
                    "qtd_tickets": {"$sum": 1},
                    "total_horas_solicitadas": {
                        "$sum": {"$ifNull": ["$horas_solicitadas", 0]}
                    },
                    "horas_validadas_aprovadas": {
                        "$sum": {
                            "$cond": [
                                {"$eq": ["$status", "APROVADO"]},
                                {"$ifNull": ["$horas_validadas", 0]},
                                0,
                            ]
                        }
                    },
                }
            },
            {
                "$lookup": {
                    "from": "alunos",
                    "localField": "_id",
                    "foreignField": "matricula",
                    "as": "aluno",
                }
            },
            {"$unwind": "$aluno"},
            {
                "$lookup": {
                    "from": "cursos",
                    "localField": "aluno.id_curso",
                    "foreignField": "id_curso",
                    "as": "curso",
                }
            },
            {"$unwind": "$curso"},
            {
                "$project": {
                    "_id": 0,
                    "matricula": "$_id",
                    "nome_aluno": "$aluno.nome_aluno",
                    "nome_curso": "$curso.nome_curso",
                    "qtd_tickets": 1,
                    "horas_solicitadas": "$total_horas_solicitadas",
                    "horas_validadas": "$horas_validadas_aprovadas",
                    "horas_exigidas": "$curso.horas_exigidas",
                    "percentual_concluido": {
                        "$cond": [
                            {"$gt": ["$curso.horas_exigidas", 0]},
                            {
                                "$round": [
                                    {
                                        "$multiply": [
                                            {
                                                "$divide": [
                                                    "$horas_validadas_aprovadas",
                                                    "$curso.horas_exigidas",
                                                ]
                                            },
                                            100,
                                        ]
                                    },
                                    2,
                                ]
                            },
                            0,
                        ]
                    },
                    "horas_restantes": {
                        "$max": [
                            {
                                "$subtract": [
                                    "$curso.horas_exigidas",
                                    "$horas_validadas_aprovadas",
                                ]
                            },
                            0,
                        ]
                    },
                }
            },
            {"$sort": {"matricula": ASCENDING}},
        ]

        mongo = MongoQueries()
        mongo.connect()
        try:
            resultados = list(mongo.db["tickets_atividades"].aggregate(pipeline))
        finally:
            mongo.close()

        self._exibir_resultados("Horas Complementares por Aluno", resultados)

    def get_relatorio_tickets_por_categoria(self):
        """Agrupa os tickets por categoria e totaliza suas horas."""
        pipeline = [
            {
                "$group": {
                    "_id": "$id_categoria",
                    "qtd_tickets": {"$sum": 1},
                    "total_horas_solicitadas": {"$sum": "$horas_solicitadas"},
                    "total_horas_validadas": {"$sum": "$horas_validadas"},
                }
            },
            {
                "$lookup": {
                    "from": "categorias_atividade",
                    "localField": "_id",
                    "foreignField": "id_categoria",
                    "as": "categoria",
                }
            },
            {"$unwind": "$categoria"},
            {
                "$project": {
                    "_id": 0,
                    "id_categoria": "$_id",
                    "nome_categoria": "$categoria.nome_categoria",
                    "qtd_tickets": 1,
                    "total_horas_solicitadas": 1,
                    "total_horas_validadas": 1,
                }
            },
            {"$sort": {"id_categoria": ASCENDING}},
        ]

        mongo = MongoQueries()
        mongo.connect()
        try:
            resultados = list(mongo.db["tickets_atividades"].aggregate(pipeline))
        finally:
            mongo.close()

        self._exibir_resultados("Tickets por Categoria", resultados)

    def get_relatorio_tickets_por_status(self):
        """Agrupa os tickets por status e totaliza quantidade e horas."""
        pipeline = [
            {
                "$group": {
                    "_id": "$status",
                    "qtd_tickets": {"$sum": 1},
                    "total_horas_solicitadas": {"$sum": "$horas_solicitadas"},
                    "total_horas_validadas": {"$sum": "$horas_validadas"},
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "status": "$_id",
                    "qtd_tickets": 1,
                    "total_horas_solicitadas": 1,
                    "total_horas_validadas": 1,
                }
            },
            {"$sort": {"status": ASCENDING}},
        ]

        mongo = MongoQueries()
        mongo.connect()
        try:
            resultados = list(mongo.db["tickets_atividades"].aggregate(pipeline))
        finally:
            mongo.close()

        self._exibir_resultados("Tickets por Status", resultados)

    # ------------------------------------------------------------------
    # Relatórios com Junção de Coleções ($lookup - Item 7.a.1.ii)
    # ------------------------------------------------------------------

    def get_relatorio_tickets_detalhado(self):
        """Junta tickets com dados de alunos, cursos, categorias e avaliadores."""
        pipeline = [
            {
                "$lookup": {
                    "from": "alunos",
                    "localField": "matricula_aluno",
                    "foreignField": "matricula",
                    "as": "aluno",
                }
            },
            {"$unwind": "$aluno"},
            {
                "$lookup": {
                    "from": "cursos",
                    "localField": "aluno.id_curso",
                    "foreignField": "id_curso",
                    "as": "curso",
                }
            },
            {"$unwind": "$curso"},
            {
                "$lookup": {
                    "from": "categorias_atividade",
                    "localField": "id_categoria",
                    "foreignField": "id_categoria",
                    "as": "categoria",
                }
            },
            {"$unwind": "$categoria"},
            {
                "$lookup": {
                    "from": "administradores",
                    "localField": "id_admin_avaliador",
                    "foreignField": "id_admin",
                    "as": "administrador",
                }
            },
            {
                "$unwind": {
                    "path": "$administrador",
                    "preserveNullAndEmptyArrays": True,
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "id_ticket": 1,
                    "titulo": 1,
                    "nome_aluno": "$aluno.nome_aluno",
                    "nome_curso": "$curso.nome_curso",
                    "nome_categoria": "$categoria.nome_categoria",
                    "horas_solicitadas": 1,
                    "horas_validadas": 1,
                    "status": 1,
                    "avaliador": {
                        "$ifNull": ["$administrador.nome_admin", "Sem avaliador"]
                    },
                    "observacao_admin": 1,
                }
            },
            {"$sort": {"id_ticket": ASCENDING}},
        ]

        mongo = MongoQueries()
        mongo.connect()
        try:
            resultados = list(mongo.db["tickets_atividades"].aggregate(pipeline))
        finally:
            mongo.close()

        self._exibir_resultados("Tickets Detalhados", resultados)

    def get_relatorio_alunos_e_cursos(self):
        """Junta cada aluno ao curso correspondente."""
        pipeline = [
            {
                "$lookup": {
                    "from": "cursos",
                    "localField": "id_curso",
                    "foreignField": "id_curso",
                    "as": "curso",
                }
            },
            {"$unwind": "$curso"},
            {
                "$project": {
                    "_id": 0,
                    "matricula": 1,
                    "nome_aluno": 1,
                    "email": 1,
                    "periodo": 1,
                    "nome_curso": "$curso.nome_curso",
                    "horas_exigidas": "$curso.horas_exigidas",
                    "coordenador": "$curso.coordenador",
                }
            },
            {"$sort": {"matricula": ASCENDING}},
        ]

        mongo = MongoQueries()
        mongo.connect()
        try:
            resultados = list(mongo.db["alunos"].aggregate(pipeline))
        finally:
            mongo.close()

        self._exibir_resultados("Alunos e Cursos", resultados)

    # ------------------------------------------------------------------
    # Relatórios de Listagem Simples das Coleções
    # ------------------------------------------------------------------

    def get_relatorio_cursos(self):
        """Lista todos os cursos cadastrados na coleção ``cursos``."""
        mongo = MongoQueries()
        mongo.connect()
        try:
            resultados = list(
                mongo.db["cursos"]
                .find({}, {"_id": 0})
                .sort("id_curso", ASCENDING)
            )
        finally:
            mongo.close()

        self._exibir_resultados("Cursos Cadastrados", resultados)

    def get_relatorio_categorias(self):
        """Lista todas as categorias cadastradas na coleção ``categorias_atividade``."""
        mongo = MongoQueries()
        mongo.connect()
        try:
            resultados = list(
                mongo.db["categorias_atividade"]
                .find({}, {"_id": 0})
                .sort("id_categoria", ASCENDING)
            )
        finally:
            mongo.close()

        self._exibir_resultados("Categorias de Atividade", resultados)

    def get_relatorio_administradores(self):
        """Lista todos os administradores cadastrados na coleção ``administradores``."""
        mongo = MongoQueries()
        mongo.connect()
        try:
            resultados = list(
                mongo.db["administradores"]
                .find({}, {"_id": 0})
                .sort("id_admin", ASCENDING)
            )
        finally:
            mongo.close()

        self._exibir_resultados("Administradores", resultados)
