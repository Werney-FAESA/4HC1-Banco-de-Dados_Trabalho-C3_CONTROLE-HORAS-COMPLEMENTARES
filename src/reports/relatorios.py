"""Módulo de Relatórios do Sistema utilizando Aggregation Pipeline do MongoDB.

Responsável: Membro 4 (Daniel Lima Del'Antonio)

Requisitos obrigatórios do Edital C3 (Item 7.a.1 - 1,5 pontos):
- (i) Consultas realizando a sumarização / agrupamento (``$group``) de coleções (1,0 pt);
- (ii) Consultas realizando a junção de coleções (``$lookup``) (0,5 pt).
"""

from __future__ import annotations

import pandas as pd
from pymongo import ASCENDING, DESCENDING

from conexion.mongo_queries import MongoQueries


class Relatorio:
    def __init__(self):
        pass

    # ------------------------------------------------------------------
    # Relatórios de Sumarização / Agrupamento ($group - Item 7.a.1.i)
    # ------------------------------------------------------------------

    def get_relatorio_horas_por_aluno(self):
        """Agrupa os tickets por aluno ($group) somando horas solicitadas, horas validadas
        e quantidade de tickets, juntando ($lookup) com ``alunos`` e ``cursos`` para exibir
        o progresso em relação às ``horas_exigidas`` do curso.
        """
        # TODO (Membro 4 - Daniel): Implementar pipeline com $group e $lookup em tickets_atividades / alunos / cursos
        print("[TODO - Membro 4 (Daniel)] Implementar get_relatorio_horas_por_aluno() ($group + $lookup).")
        input("Pressione Enter para sair do relatório...")

    def get_relatorio_tickets_por_categoria(self):
        """Agrupa os tickets por categoria ($group) somando quantidade de tickets,
        total de horas solicitadas e total de horas validadas.
        """
        # TODO (Membro 4 - Daniel): Implementar pipeline com $group por id_categoria e $lookup em categorias_atividade
        print("[TODO - Membro 4 (Daniel)] Implementar get_relatorio_tickets_por_categoria() ($group).")
        input("Pressione Enter para sair do relatório...")

    def get_relatorio_tickets_por_status(self):
        """Agrupa os tickets por ``status`` (APROVADO, PENDENTE, RECUSADO) usando ``$group``."""
        # TODO (Membro 4 - Daniel): Implementar pipeline com $group por status
        print("[TODO - Membro 4 (Daniel)] Implementar get_relatorio_tickets_por_status() ($group).")
        input("Pressione Enter para sair do relatório...")

    # ------------------------------------------------------------------
    # Relatórios com Junção de Coleções ($lookup - Item 7.a.1.ii)
    # ------------------------------------------------------------------

    def get_relatorio_tickets_detalhado(self):
        """Junção ($lookup) de ``tickets_atividades`` com ``alunos``, ``cursos``,
        ``categorias_atividade`` e ``administradores``.
        """
        # TODO (Membro 4 - Daniel): Implementar pipeline com múltiplos $lookup e $unwind (preserveNullAndEmptyArrays no admin)
        print("[TODO - Membro 4 (Daniel)] Implementar get_relatorio_tickets_detalhado() ($lookup).")
        input("Pressione Enter para sair do relatório...")

    def get_relatorio_alunos_e_cursos(self):
        """Junção ($lookup) da coleção ``alunos`` com a coleção ``cursos``."""
        # TODO (Membro 4 - Daniel): Implementar pipeline em alunos com $lookup para cursos
        print("[TODO - Membro 4 (Daniel)] Implementar get_relatorio_alunos_e_cursos() ($lookup).")
        input("Pressione Enter para sair do relatório...")

    # ------------------------------------------------------------------
    # Relatórios de Listagem Simples das Coleções
    # ------------------------------------------------------------------

    def get_relatorio_cursos(self):
        """Lista todos os cursos cadastrados na coleção ``cursos``."""
        # TODO (Membro 4 - Daniel): Implementar find({}, {"_id": 0}).sort("id_curso", ASCENDING)
        print("[TODO - Membro 4 (Daniel)] Implementar get_relatorio_cursos().")
        input("Pressione Enter para sair do relatório...")

    def get_relatorio_categorias(self):
        """Lista todas as categorias cadastradas na coleção ``categorias_atividade``."""
        # TODO (Membro 4 - Daniel): Implementar find({}, {"_id": 0}).sort("id_categoria", ASCENDING)
        print("[TODO - Membro 4 (Daniel)] Implementar get_relatorio_categorias().")
        input("Pressione Enter para sair do relatório...")

    def get_relatorio_administradores(self):
        """Lista todos os administradores cadastrados na coleção ``administradores``."""
        # TODO (Membro 4 - Daniel): Implementar find({}, {"_id": 0}).sort("id_admin", ASCENDING)
        print("[TODO - Membro 4 (Daniel)] Implementar get_relatorio_administradores().")
        input("Pressione Enter para sair do relatório...")
