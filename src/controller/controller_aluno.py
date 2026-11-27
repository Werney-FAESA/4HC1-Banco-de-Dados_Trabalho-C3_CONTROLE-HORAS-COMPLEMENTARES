"""Operações CRUD da coleção ``alunos`` no MongoDB.

Responsável: Membro 2 (Issacar Mattos Gutler)
"""

from __future__ import annotations
from typing import Optional

import pandas as pd
from pymongo import ASCENDING

from conexion.mongo_queries import MongoQueries
from model.aluno import Aluno
from model.curso import Curso
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Aluno:
    """Controla a inclusão, listagem, alteração e exclusão de Alunos no MongoDB."""

    COLLECTION_NAME = "alunos"
    COLLECTION_CURSOS = "cursos"

    def __init__(self):
        self.mongo = MongoQueries()

    @staticmethod
    def _ler_inteiro(
        mensagem: str,
        positivo: bool = True,
        valor_atual: Optional[int] = None,
    ) -> int:
        """Lê um inteiro, permitindo manter ``valor_atual`` com Enter na edição."""
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
        """Lê um texto obrigatório, mantendo ``valor_atual`` com Enter na edição."""
        while True:
            entrada = input(mensagem).strip()
            if not entrada and valor_atual is not None:
                return valor_atual
            if entrada:
                return entrada
            print("Entrada inválida. O campo não pode ficar em branco.")

    def _buscar_documento(self, matricula: int) -> Optional[dict]:
        self.mongo.connect()
        try:
            return self.mongo.db[self.COLLECTION_NAME].find_one(
                {"matricula": matricula}, {"_id": 0}
            )
        finally:
            self.mongo.close()

    def _buscar_curso(self, id_curso: int) -> Optional[dict]:
        """Busca o curso usado como FK lógica no documento de aluno."""
        self.mongo.connect()
        try:
            return self.mongo.db[self.COLLECTION_CURSOS].find_one(
                {"id_curso": id_curso}, {"_id": 0}
            )
        finally:
            self.mongo.close()

    @staticmethod
    def _instanciar_curso(documento: Optional[dict]) -> Optional[Curso]:
        if not documento:
            return None
        return Curso(
            id_curso=documento.get("id_curso"),
            nome_curso=documento.get("nome_curso"),
            horas_exigidas=documento.get("horas_exigidas"),
            coordenador=documento.get("coordenador"),
        )

    @classmethod
    def _instanciar_aluno(
        cls,
        documento: dict,
        documento_curso: Optional[dict] = None,
    ) -> Aluno:
        """Monta o objeto de domínio sem gravar o curso dentro de ``alunos``."""
        return Aluno(
            matricula=documento.get("matricula"),
            nome_aluno=documento.get("nome_aluno"),
            email=documento.get("email"),
            periodo=documento.get("periodo"),
            curso=cls._instanciar_curso(documento_curso),
        )

    def _listar_cursos_disponiveis(self) -> bool:
        """Exibe os cursos para que o usuário possa selecionar uma FK válida."""
        self.mongo.connect()
        try:
            cursos = list(
                self.mongo.db[self.COLLECTION_CURSOS]
                .find({}, {"_id": 0})
                .sort("id_curso", ASCENDING)
            )
        finally:
            self.mongo.close()

        if not cursos:
            print("Nenhum curso cadastrado. Cadastre um curso antes de cadastrar alunos.")
            return False

        print("\n=== Cursos Disponíveis ===")
        print(pd.DataFrame(cursos).to_string(index=False))
        return True

    def listar_alunos(self) -> bool:
        """Lista os alunos com o nome do curso associado ($lookup em ``cursos``)."""
        pipeline = [
            {
                "$lookup": {
                    "from": self.COLLECTION_CURSOS,
                    "localField": "id_curso",
                    "foreignField": "id_curso",
                    "as": "curso",
                }
            },
            {
                "$unwind": {
                    "path": "$curso",
                    "preserveNullAndEmptyArrays": True,
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "matricula": 1,
                    "nome_aluno": 1,
                    "email": 1,
                    "periodo": 1,
                    "id_curso": 1,
                    "nome_curso": "$curso.nome_curso",
                }
            },
            {"$sort": {"matricula": ASCENDING}},
        ]

        self.mongo.connect()
        try:
            alunos = list(self.mongo.db[self.COLLECTION_NAME].aggregate(pipeline))
        finally:
            self.mongo.close()

        if not alunos:
            print("Nenhum aluno cadastrado na coleção 'alunos'.")
            return False

        print("\n=== Alunos Cadastrados ===")
        print(pd.DataFrame(alunos).to_string(index=False))
        return True

    def verifica_existencia(self, matricula: int) -> bool:
        """Retorna True se já existir um aluno com ``matricula`` na coleção ``alunos``."""
        return self._buscar_documento(matricula) is not None

    def inserir_aluno(self) -> Optional[Aluno]:
        """Coleta os dados no console, valida o ``id_curso`` em ``cursos`` e insere o aluno."""
        matricula = self._ler_inteiro("Matrícula (número inteiro positivo): ")
        if self.verifica_existencia(matricula):
            print(f"Já existe um aluno cadastrado com a matrícula {matricula}.")
            return None

        nome_aluno = self._ler_texto("Nome do Aluno: ")
        email = self._ler_texto("E-mail: ")
        periodo = self._ler_inteiro("Período (número inteiro positivo): ")

        if not self._listar_cursos_disponiveis():
            return None
        id_curso = self._ler_inteiro("ID do Curso: ")
        curso = self._buscar_curso(id_curso)
        if not curso:
            print(f"O curso com ID {id_curso} não existe.")
            return None

        novo_documento = {
            "matricula": matricula,
            "nome_aluno": nome_aluno,
            "email": email,
            "periodo": periodo,
            "id_curso": id_curso,
        }

        self.mongo.connect()
        try:
            self.mongo.db[self.COLLECTION_NAME].insert_one(dict(novo_documento))
        finally:
            self.mongo.close()

        aluno = self._instanciar_aluno(novo_documento, curso)
        print("\nAluno cadastrado com sucesso!")
        print(aluno.to_string())
        return aluno

    def atualizar_aluno(self) -> Optional[Aluno]:
        """Lista os alunos, solicita a ``matricula``, atualiza via ``update_one`` e exibe o aluno atualizado."""
        if not self.listar_alunos():
            return None

        matricula = self._ler_inteiro("\nInforme a matrícula do aluno que deseja alterar: ")
        doc_atual = self._buscar_documento(matricula)
        if not doc_atual:
            print(f"O aluno com matrícula {matricula} não existe.")
            return None

        print("\nPressione Enter para manter o valor atual.")
        nome_aluno = self._ler_texto(
            f"Nome do Aluno [{doc_atual['nome_aluno']}]: ",
            valor_atual=doc_atual["nome_aluno"],
        )
        email = self._ler_texto(
            f"E-mail [{doc_atual['email']}]: ",
            valor_atual=doc_atual["email"],
        )
        periodo = self._ler_inteiro(
            f"Período [{doc_atual['periodo']}]: ",
            valor_atual=doc_atual["periodo"],
        )

        if not self._listar_cursos_disponiveis():
            return None
        id_curso = self._ler_inteiro(
            f"ID do Curso [{doc_atual['id_curso']}]: ",
            valor_atual=doc_atual["id_curso"],
        )
        curso = self._buscar_curso(id_curso)
        if not curso:
            print(f"O curso com ID {id_curso} não existe.")
            return None

        novos_dados = {
            "nome_aluno": nome_aluno,
            "email": email,
            "periodo": periodo,
            "id_curso": id_curso,
        }
        self.mongo.connect()
        try:
            self.mongo.db[self.COLLECTION_NAME].update_one(
                {"matricula": matricula},
                {"$set": novos_dados},
            )
        finally:
            self.mongo.close()

        aluno_atualizado = self._instanciar_aluno(
            {"matricula": matricula, **novos_dados}, curso
        )
        print("\nAluno atualizado com sucesso!")
        print(aluno_atualizado.to_string())
        return aluno_atualizado

    def excluir_aluno(self) -> bool:
        """Lista os alunos e exclui um documento usando ``excluir_registro_seguro``."""
        if not self.listar_alunos():
            return False

        matricula = self._ler_inteiro("\nInforme a matrícula do aluno que deseja excluir: ")
        doc_atual = self._buscar_documento(matricula)
        if not doc_atual:
            print(f"O aluno com matrícula {matricula} não existe.")
            return False

        return excluir_registro_seguro(
            self.COLLECTION_NAME,
            matricula,
            f"o aluno '{doc_atual['nome_aluno']}'",
        )
