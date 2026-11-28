"""Operações CRUD da coleção ``administradores`` no MongoDB.

Responsável: Membro 4 (Daniel Lima Del'Antonio)
"""

from __future__ import annotations
from typing import Optional

import pandas as pd
from pymongo import ASCENDING

from conexion.mongo_queries import MongoQueries
from model.administrador import Administrador
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Administrador:
    """Controla a inclusão, listagem, alteração e exclusão de Administradores no MongoDB."""

    COLLECTION_NAME = "administradores"

    def __init__(self):
        self.mongo = MongoQueries()

    @staticmethod
    def _ler_inteiro(
        mensagem: str,
        positivo: bool = True
    ) -> int:
        while True:
            entrada = input(mensagem).strip()
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
        while True:
            entrada = input(mensagem).strip()
            if not entrada and valor_atual is not None:
                return valor_atual
            if entrada:
                return entrada
            print("Entrada inválida. O campo não pode ficar em branco.")

    def _buscar_documento(self, id_admin: int) -> Optional[dict]:
        self.mongo.connect()
        try:
            return self.mongo.db[self.COLLECTION_NAME].find_one(
                {"id_admin": id_admin}, {"_id": 0}
            )
        finally:
            self.mongo.close()

    def _buscar_por_email(self, email: str) -> Optional[dict]:
        self.mongo.connect()
        try:
            return self.mongo.db[self.COLLECTION_NAME].find_one(
                {"email": email}, {"_id": 0}
            )
        finally:
            self.mongo.close()

    @staticmethod
    def _instanciar_administrador(documento: dict) -> Administrador:
        return Administrador(
            id_admin=documento.get("id_admin"),
            nome_admin=documento.get("nome_admin"),
            email=documento.get("email"),
            cargo=documento.get("cargo"),
        )

    def listar_administradores(self) -> bool:
        self.mongo.connect()
        try:
            administradores = list(
                self.mongo.db[self.COLLECTION_NAME]
                .find({}, {"_id": 0})
                .sort("id_admin", ASCENDING)
            )
        finally:
            self.mongo.close()

        if not administradores:
            print("Nenhum administrador cadastrado na coleção 'administradores'.")
            return False

        print("\n=== Administradores Cadastrados ===")
        print(pd.DataFrame(administradores).to_string(index=False))
        return True

    def verifica_existencia(self, id_admin: int) -> bool:
        return self._buscar_documento(id_admin) is not None

    def inserir_administrador(self) -> Optional[Administrador]:
        id_admin = self._ler_inteiro("ID do Administrador (número inteiro positivo): ")
        if self.verifica_existencia(id_admin):
            print(f"Já existe um administrador cadastrado com o ID {id_admin}.")
            return None

        nome_admin = self._ler_texto("Nome do Administrador: ")
        email = self._ler_texto("E-mail: ")
        if self._buscar_por_email(email):
            print(f"Já existe um administrador cadastrado com o e-mail '{email}'.")
            return None
        cargo = self._ler_texto("Cargo: ")

        novo_documento = {
            "id_admin": id_admin,
            "nome_admin": nome_admin,
            "email": email,
            "cargo": cargo,
        }

        self.mongo.connect()
        try:
            self.mongo.db[self.COLLECTION_NAME].insert_one(dict(novo_documento))
        finally:
            self.mongo.close()

        administrador = self._instanciar_administrador(novo_documento)
        print("\nAdministrador cadastrado com sucesso!")
        print(administrador.to_string())
        return administrador

    def atualizar_administrador(self) -> Optional[Administrador]:
        if not self.listar_administradores():
            return None

        id_admin = self._ler_inteiro(
            "\nInforme o ID do administrador que deseja alterar: "
        )
        documento_atual = self._buscar_documento(id_admin)
        if not documento_atual:
            print(f"O administrador com ID {id_admin} não existe.")
            return None

        print("\nPressione Enter para manter o valor atual.")
        nome_admin = self._ler_texto(
            f"Nome do Administrador [{documento_atual['nome_admin']}]: ",
            valor_atual=documento_atual["nome_admin"],
        )
        email = self._ler_texto(
            f"E-mail [{documento_atual['email']}]: ",
            valor_atual=documento_atual["email"],
        )
        if email != documento_atual["email"]:
            documento_email = self._buscar_por_email(email)
            if documento_email and documento_email["id_admin"] != id_admin:
                print(f"Já existe um administrador cadastrado com o e-mail '{email}'.")
                return None
        cargo = self._ler_texto(
            f"Cargo [{documento_atual['cargo']}]: ",
            valor_atual=documento_atual["cargo"],
        )

        novos_dados = {
            "nome_admin": nome_admin,
            "email": email,
            "cargo": cargo,
        }

        self.mongo.connect()
        try:
            self.mongo.db[self.COLLECTION_NAME].update_one(
                {"id_admin": id_admin},
                {"$set": novos_dados},
            )
        finally:
            self.mongo.close()

        administrador_atualizado = self._instanciar_administrador(
            {"id_admin": id_admin, **novos_dados}
        )
        print("\nAdministrador atualizado com sucesso!")
        print(administrador_atualizado.to_string())
        return administrador_atualizado

    def excluir_administrador(self) -> bool:
        if not self.listar_administradores():
            return False

        id_admin = self._ler_inteiro(
            "\nInforme o ID do administrador que deseja excluir: "
        )
        documento_atual = self._buscar_documento(id_admin)
        if not documento_atual:
            print(f"O administrador com ID {id_admin} não existe.")
            return False

        return excluir_registro_seguro(
            self.COLLECTION_NAME,
            id_admin,
            f"o administrador '{documento_atual['nome_admin']}'",
        )
