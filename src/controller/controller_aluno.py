"""Operações CRUD da coleção ``alunos`` no MongoDB.

Responsável: Membro 2 (Issacar Mattos Gutler)
"""

from __future__ import annotations
from typing import Optional

import pandas as pd

from conexion.mongo_queries import MongoQueries
from model.aluno import Aluno
from model.curso import Curso
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Aluno:
    """Controla a inclusão, listagem, alteração e exclusão de Alunos no MongoDB."""

    def __init__(self):
        self.mongo = MongoQueries()

    def listar_alunos(self) -> bool:
        """Lista os alunos com o nome do curso associado ($lookup em ``cursos``)."""
        # TODO (Membro 2 - Issacar): Implementar listagem de alunos com $lookup na coleção 'cursos'
        print("[TODO - Membro 2 (Issacar)] Implementar listar_alunos() na coleção 'alunos'.")
        return False

    def verifica_existencia(self, matricula: int) -> bool:
        """Retorna True se já existir um aluno com ``matricula`` na coleção ``alunos``."""
        # TODO (Membro 2 - Issacar): Consultar self.mongo.db["alunos"].find_one({"matricula": matricula})
        return False

    def inserir_aluno(self) -> Optional[Aluno]:
        """Coleta os dados no console, valida o ``id_curso`` em ``cursos`` e insere o aluno."""
        # TODO (Membro 2 - Issacar): Implementar inserção com validação de FK id_curso e retornar Aluno
        print("[TODO - Membro 2 (Issacar)] Implementar inserir_aluno().")
        return None

    def atualizar_aluno(self) -> Optional[Aluno]:
        """Lista os alunos, solicita a ``matricula``, atualiza via ``update_one`` e exibe o aluno atualizado."""
        # TODO (Membro 2 - Issacar): Implementar atualização com update_one({"matricula": matricula}, {"$set": ...})
        print("[TODO - Membro 2 (Issacar)] Implementar atualizar_aluno().")
        return None

    def excluir_aluno(self) -> bool:
        """Lista os alunos e exclui um documento usando ``excluir_registro_seguro``."""
        # TODO (Membro 2 - Issacar): Listar alunos, ler matricula e chamar excluir_registro_seguro("alunos", matricula, ...)
        print("[TODO - Membro 2 (Issacar)] Implementar excluir_aluno().")
        return False
