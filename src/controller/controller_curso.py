"""Operações CRUD da coleção ``cursos`` no MongoDB.

Responsável: Membro 1 (Kaike Vaccari do Nascimento)
"""

from __future__ import annotations
from typing import Optional

import pandas as pd

from conexion.mongo_queries import MongoQueries
from model.curso import Curso
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Curso:
    """Controla a inclusão, listagem, alteração e exclusão de Cursos no MongoDB."""

    def __init__(self):
        self.mongo = MongoQueries()

    def listar_cursos(self) -> bool:
        """Lista os documentos da coleção ``cursos`` ordenados por ``id_curso``."""
        # TODO (Membro 1 - Kaike): Buscar em self.mongo.db["cursos"].find(..., {"_id": 0}) e exibir DataFrame
        print("[TODO - Membro 1 (Kaike)] Implementar listar_cursos() na coleção 'cursos'.")
        return False

    def verifica_existencia(self, id_curso: int) -> bool:
        """Retorna True se já existir um curso com ``id_curso`` na coleção ``cursos``."""
        # TODO (Membro 1 - Kaike): Consultar self.mongo.db["cursos"].find_one({"id_curso": id_curso})
        return False

    def inserir_curso(self) -> Optional[Curso]:
        """Coleta os dados no console e insere um novo documento na coleção ``cursos``."""
        # TODO (Membro 1 - Kaike): Implementar inserção com insert_one e retornar instância de Curso
        print("[TODO - Membro 1 (Kaike)] Implementar inserir_curso().")
        return None

    def atualizar_curso(self) -> Optional[Curso]:
        """Lista os cursos, solicita o ``id_curso``, atualiza via ``update_one`` e exibe o curso atualizado."""
        # TODO (Membro 1 - Kaike): Implementar atualização com update_one({"id_curso": id_curso}, {"$set": ...})
        print("[TODO - Membro 1 (Kaike)] Implementar atualizar_curso().")
        return None

    def excluir_curso(self) -> bool:
        """Lista os cursos e exclui um documento usando ``excluir_registro_seguro``."""
        # TODO (Membro 1 - Kaike): Listar cursos, ler id_curso e chamar excluir_registro_seguro("cursos", id_curso, ...)
        print("[TODO - Membro 1 (Kaike)] Implementar excluir_curso().")
        return False
