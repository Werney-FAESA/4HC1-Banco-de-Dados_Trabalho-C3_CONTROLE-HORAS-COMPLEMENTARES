"""Operações CRUD da coleção ``categorias_atividade`` no MongoDB.

Responsável: Membro 3 (Bruno Mauro Bayer Laiber)
"""

from __future__ import annotations
from typing import Optional

import pandas as pd

from conexion.mongo_queries import MongoQueries
from model.categoria_atividade import CategoriaAtividade
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Categoria_Atividade:
    """Controla a inclusão, listagem, alteração e exclusão de Categorias de Atividade no MongoDB."""

    def __init__(self):
        self.mongo = MongoQueries()

    def listar_categorias(self) -> bool:
        """Lista os documentos da coleção ``categorias_atividade`` ordenados por ``id_categoria``."""
        # TODO (Membro 3 - Bruno): Buscar em self.mongo.db["categorias_atividade"].find(..., {"_id": 0})
        print("[TODO - Membro 3 (Bruno)] Implementar listar_categorias() na coleção 'categorias_atividade'.")
        return False

    def verifica_existencia(self, id_categoria: int) -> bool:
        """Retorna True se já existir uma categoria com ``id_categoria``."""
        # TODO (Membro 3 - Bruno): Consultar self.mongo.db["categorias_atividade"].find_one({"id_categoria": id_categoria})
        return False

    def inserir_categoria(self) -> Optional[CategoriaAtividade]:
        """Coleta os dados no console e insere uma nova categoria na coleção ``categorias_atividade``."""
        # TODO (Membro 3 - Bruno): Implementar inserção com insert_one e retornar instância de CategoriaAtividade
        print("[TODO - Membro 3 (Bruno)] Implementar inserir_categoria().")
        return None

    def atualizar_categoria(self) -> Optional[CategoriaAtividade]:
        """Lista as categorias, solicita ``id_categoria``, atualiza via ``update_one`` e exibe o registro atualizado."""
        # TODO (Membro 3 - Bruno): Implementar atualização com update_one e exibir to_string()
        print("[TODO - Membro 3 (Bruno)] Implementar atualizar_categoria().")
        return None

    def excluir_categoria(self) -> bool:
        """Lista as categorias e exclui um documento usando ``excluir_registro_seguro``."""
        # TODO (Membro 3 - Bruno): Chamar excluir_registro_seguro("categorias_atividade", id_categoria, ...)
        print("[TODO - Membro 3 (Bruno)] Implementar excluir_categoria().")
        return False
