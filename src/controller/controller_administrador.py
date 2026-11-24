"""Operações CRUD da coleção ``administradores`` no MongoDB.

Responsável: Membro 4 (Daniel Lima Del'Antonio)
"""

from __future__ import annotations
from typing import Optional

import pandas as pd

from conexion.mongo_queries import MongoQueries
from model.administrador import Administrador
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Administrador:
    """Controla a inclusão, listagem, alteração e exclusão de Administradores no MongoDB."""

    def __init__(self):
        self.mongo = MongoQueries()

    def listar_administradores(self) -> bool:
        """Lista os documentos da coleção ``administradores`` ordenados por ``id_admin``."""
        # TODO (Membro 4 - Daniel): Buscar em self.mongo.db["administradores"].find(..., {"_id": 0})
        print("[TODO - Membro 4 (Daniel)] Implementar listar_administradores() na coleção 'administradores'.")
        return False

    def verifica_existencia(self, id_admin: int) -> bool:
        """Retorna True se já existir um administrador com ``id_admin``."""
        # TODO (Membro 4 - Daniel): Consultar self.mongo.db["administradores"].find_one({"id_admin": id_admin})
        return False

    def inserir_administrador(self) -> Optional[Administrador]:
        """Coleta os dados no console e insere um novo administrador na coleção ``administradores``."""
        # TODO (Membro 4 - Daniel): Implementar inserção com insert_one e retornar instância de Administrador
        print("[TODO - Membro 4 (Daniel)] Implementar inserir_administrador().")
        return None

    def atualizar_administrador(self) -> Optional[Administrador]:
        """Lista os administradores, solicita ``id_admin``, atualiza via ``update_one`` e exibe o registro atualizado."""
        # TODO (Membro 4 - Daniel): Implementar atualização com update_one e exibir to_string()
        print("[TODO - Membro 4 (Daniel)] Implementar atualizar_administrador().")
        return None

    def excluir_administrador(self) -> bool:
        """Lista os administradores e exclui um documento usando ``excluir_registro_seguro``."""
        # TODO (Membro 4 - Daniel): Chamar excluir_registro_seguro("administradores", id_admin, ...)
        print("[TODO - Membro 4 (Daniel)] Implementar excluir_administrador().")
        return False
