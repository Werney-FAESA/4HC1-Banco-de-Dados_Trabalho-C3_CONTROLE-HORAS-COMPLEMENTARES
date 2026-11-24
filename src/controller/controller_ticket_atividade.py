"""Operações CRUD da coleção ``tickets_atividades`` no MongoDB.

Responsável: Membro 6 (Gabriel Antônio Galdino dos Santos)
"""

from __future__ import annotations
from typing import Optional

import pandas as pd

from conexion.mongo_queries import MongoQueries
from model.administrador import Administrador
from model.aluno import Aluno
from model.categoria_atividade import CategoriaAtividade
from model.curso import Curso
from model.ticket_atividade import TicketAtividade
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Ticket_Atividade:
    """Controla a inclusão, listagem, alteração/avaliação e exclusão de Tickets de Atividades Complementares."""

    def __init__(self):
        self.mongo = MongoQueries()

    def listar_tickets(self) -> bool:
        """Lista os tickets da coleção ``tickets_atividades`` com dados do aluno e da categoria ($lookup)."""
        # TODO (Membro 6 - Gabriel): Implementar listagem de tickets com $lookup em alunos e categorias_atividade
        print("[TODO - Membro 6 (Gabriel)] Implementar listar_tickets() na coleção 'tickets_atividades'.")
        return False

    def verifica_existencia(self, id_ticket: int) -> bool:
        """Retorna True se já existir um ticket com ``id_ticket``."""
        # TODO (Membro 6 - Gabriel): Consultar self.mongo.db["tickets_atividades"].find_one({"id_ticket": id_ticket})
        return False

    def inserir_ticket(self) -> Optional[TicketAtividade]:
        """Coleta os dados no console, valida referências e teto de horas da categoria e insere o ticket."""
        # TODO (Membro 6 - Gabriel):
        # 1. Validar se id_ticket já existe
        # 2. Listar alunos e validar matricula_aluno
        # 3. Listar categorias_atividade, validar id_categoria e verificar limite_maximo_horas
        # 4. Ler titulo, horas_solicitadas, status (PENDENTE/APROVADO/RECUSADO), id_admin_avaliador, horas_validadas e observacao_admin
        # 5. Inserir com insert_one e retornar instância de TicketAtividade exibindo to_string()
        print("[TODO - Membro 6 (Gabriel)] Implementar inserir_ticket().")
        return None

    def atualizar_ticket(self) -> Optional[TicketAtividade]:
        """Permite atualizar os dados ou avaliar (aprovar/recusar) um ticket existente via ``update_one``."""
        # TODO (Membro 6 - Gabriel): Implementar atualização de ticket e exibir to_string() do documento atualizado
        print("[TODO - Membro 6 (Gabriel)] Implementar atualizar_ticket().")
        return None

    def excluir_ticket(self) -> bool:
        """Lista os tickets e exclui o documento selecionado usando ``excluir_registro_seguro``."""
        # TODO (Membro 6 - Gabriel): Chamar excluir_registro_seguro("tickets_atividades", id_ticket, ...)
        print("[TODO - Membro 6 (Gabriel)] Implementar excluir_ticket().")
        return False
