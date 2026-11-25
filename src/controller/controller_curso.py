"""Operações CRUD da coleção ``cursos`` no MongoDB.

Responsável: Membro 1 (Kaike Vaccari do Nascimento)
"""

from __future__ import annotations
from typing import Optional

import pandas as pd
from pymongo import ASCENDING

from conexion.mongo_queries import MongoQueries
from model.curso import Curso
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Curso:
    """Controla a inclusão, listagem, alteração e exclusão de Cursos no MongoDB."""

    COLLECTION_NAME = "cursos"

    def __init__(self):
        self.mongo = MongoQueries()

    @staticmethod
    def _ler_inteiro(
        mensagem: str,
        positivo: bool = True,
        valor_atual: Optional[int] = None,
    ) -> int:
        while True:
            entrada = input(mensagem).strip()
            if not entrada and valor_atual is not None:
                return valor_atual
            try:
                valor = int(entrada)
            except ValueError:
                print("Valor inválido. Informe um número inteiro.")
                continue
            if positivo and valor <= 0:
                print("Valor inválido. Informe um número inteiro maior que zero.")
                continue
            return valor

    @staticmethod
    def _ler_texto(mensagem: str, valor_atual: Optional[str] = None) -> str:
            entrada = input(mensagem).strip()
            if not entrada and valor_atual is not None:
                return valor_atual
            if entrada:
                return entrada
            print("Entrada inválida. O campo não pode ficar em branco.")

    def _buscar_documento(self, id_curso: int) -> Optional[dict]:
        self.mongo.connect()
        try:
            return self.mongo.db[self.COLLECTION_NAME].find_one(
                {"id_curso": id_curso}, {"_id": 0}
            )
        finally:
            self.mongo.close()

    @staticmethod
    def _instanciar_curso(documento: dict) -> Curso:
        return Curso(
            id_curso=documento.get("id_curso"),
            nome_curso=documento.get("nome_curso"),
            horas_exigidas=documento.get("horas_exigidas"),
            coordenador=documento.get("coordenador"),
        )

    def listar_cursos(self) -> bool:
        self.mongo.connect()
        try:
            cursos = list(
                self.mongo.db[self.COLLECTION_NAME]
                .find({}, {"_id": 0})
                .sort("id_curso", ASCENDING)
            )
        finally:
            self.mongo.close()

        if not cursos:
            print("Nenhum curso cadastrado na coleção 'cursos'.")
            return False

        df_cursos = pd.DataFrame(cursos)
        print("\n=== Cursos Cadastrados ===")
        print(df_cursos.to_string(index=False))
        return True

    def verifica_existencia(self, id_curso: int) -> bool:
        return self._buscar_documento(id_curso) is not None

    def inserir_curso(self) -> Optional[Curso]:
        id_curso = self._ler_inteiro("ID do Curso (número inteiro positivo): ")
        if self.verifica_existencia(id_curso):
            print(f"Já existe um curso cadastrado com o ID {id_curso}.")
            return None

        nome_curso = self._ler_texto("Nome do Curso: ")
        horas_exigidas = self._ler_inteiro("Total de Horas Exigidas: ")
        coordenador = self._ler_texto("Nome do Coordenador: ")

        novo_documento = {
            "id_curso": id_curso,
            "nome_curso": nome_curso,
            "horas_exigidas": horas_exigidas,
            "coordenador": coordenador,
        }

        self.mongo.connect()
        try:
            self.mongo.db[self.COLLECTION_NAME].insert_one(dict(novo_documento))
        finally:
            self.mongo.close()

        curso = self._instanciar_curso(novo_documento)
        print("\nCurso cadastrado com sucesso!")
        print(curso.to_string())
        return curso

    def atualizar_curso(self) -> Optional[Curso]:
        if not self.listar_cursos():
            return None

        id_curso = self._ler_inteiro("\nInforme o ID do curso que deseja alterar: ")
        doc_atual = self._buscar_documento(id_curso)
        if not doc_atual:
            print(f"O curso com ID {id_curso} não existe.")
            return None

        print("\nPressione Enter para manter o valor atual.")
        nome_curso = self._ler_texto(
            f"Nome do Curso [{doc_atual['nome_curso']}]: ",
            valor_atual=doc_atual["nome_curso"],
        )
        horas_exigidas = self._ler_inteiro(
            f"Horas Exigidas [{doc_atual['horas_exigidas']}]: ",
            valor_atual=doc_atual["horas_exigidas"],
        )
        coordenador = self._ler_texto(
            f"Coordenador [{doc_atual['coordenador']}]: ",
            valor_atual=doc_atual["coordenador"],
        )

        novos_dados = {
            "nome_curso": nome_curso,
            "horas_exigidas": horas_exigidas,
            "coordenador": coordenador,
        }

        self.mongo.connect()
        try:
            self.mongo.db[self.COLLECTION_NAME].update_one(
                {"id_curso": id_curso},
                {"$set": novos_dados},
            )
        finally:
            self.mongo.close()

        curso_atualizado = self._instanciar_curso({"id_curso": id_curso, **novos_dados})
        print("\nCurso atualizado com sucesso!")
        print(curso_atualizado.to_string())
        return curso_atualizado

    def excluir_curso(self) -> bool:
        if not self.listar_cursos():
            return False

        id_curso = self._ler_inteiro("\nInforme o ID do curso que deseja excluir: ")
        doc_atual = self._buscar_documento(id_curso)
        if not doc_atual:
            print(f"O curso com ID {id_curso} não existe.")
            return False

        return excluir_registro_seguro(
            self.COLLECTION_NAME,
            id_curso,
            f"o curso '{doc_atual['nome_curso']}'",
        )
