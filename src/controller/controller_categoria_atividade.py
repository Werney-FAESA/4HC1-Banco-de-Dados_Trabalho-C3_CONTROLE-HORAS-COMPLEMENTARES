"""Operações CRUD da coleção ``categorias_atividade`` no MongoDB.

Responsável: Membro 3 (Bruno Mauro Bayer Laiber)
"""

from __future__ import annotations

import pandas as pd
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError

from conexion.mongo_queries import MongoQueries
from model.categoria_atividade import CategoriaAtividade
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Categoria_Atividade:
    """Controla a inclusão, listagem, alteração e exclusão de categorias."""

    COLLECTION_NAME = "categorias_atividade"

    def __init__(self):
        self.mongo = MongoQueries()

    @staticmethod
    def _ler_inteiro(mensagem: str, valor_atual: int | None = None) -> int:
        while True:
            entrada = input(mensagem).strip()
            if not entrada and valor_atual is not None:
                return valor_atual
            try:
                valor = int(entrada)
                if 0 < valor <= 2**63 - 1:
                    return valor
            except ValueError:
                pass
            print("Informe um número inteiro positivo válido.")

    @staticmethod
    def _ler_texto(mensagem: str, valor_atual: str | None = None) -> str:
        while True:
            entrada = input(mensagem).strip()
            if not entrada and valor_atual is not None:
                return valor_atual
            if entrada:
                return entrada
            print("O campo não pode ficar em branco.")

    def _ler_dados(self, documento: dict | None = None) -> dict:
        atual = documento or {}
        nome = atual.get("nome_categoria")
        limite = atual.get("limite_maximo_horas")
        descricao = atual.get("descricao")
        return {
            "nome_categoria": self._ler_texto(
                f"Nome da categoria [{nome}]: " if nome is not None else "Nome da categoria: ",
                nome,
            ),
            "limite_maximo_horas": self._ler_inteiro(
                f"Limite máximo de horas [{limite}]: "
                if limite is not None else "Limite máximo de horas: ",
                limite,
            ),
            "descricao": self._ler_texto(
                f"Descrição [{descricao}]: " if descricao is not None else "Descrição: ",
                descricao,
            ),
        }

    def _buscar_documento(self, id_categoria: int) -> dict | None:
        try:
            self.mongo.connect()
            return self.mongo.db[self.COLLECTION_NAME].find_one(
                {"id_categoria": id_categoria}
            )
        finally:
            self.mongo.close()

    def listar_categorias(self) -> bool:
        """Lista as categorias por ordem de ID e indica se a coleção tem registros."""
        try:
            self.mongo.connect()
            categorias = list(
                self.mongo.db[self.COLLECTION_NAME]
                .find({}, {"_id": 0})
                .sort("id_categoria", ASCENDING)
            )
        finally:
            self.mongo.close()

        if not categorias:
            print("Nenhuma categoria de atividade cadastrada.")
            return False

        print("\n=== Categorias de Atividade ===")
        print(pd.DataFrame(categorias).to_string(index=False))
        return True

    def verifica_existencia(self, id_categoria: int) -> bool:
        """Retorna True se já existir uma categoria com o ID informado."""
        return self._buscar_documento(id_categoria) is not None

    def inserir_categoria(self) -> CategoriaAtividade | None:
        id_categoria = self._ler_inteiro("ID da categoria: ")
        if self.verifica_existencia(id_categoria):
            print(f"Já existe uma categoria com o ID {id_categoria}.")
            return None

        dados = {"id_categoria": id_categoria, **self._ler_dados()}
        try:
            self.mongo.connect()
            # O índice de _id evita cadastros concorrentes com o mesmo ID lógico.
            self.mongo.db[self.COLLECTION_NAME].insert_one({"_id": id_categoria, **dados})
        except DuplicateKeyError:
            print(f"Já existe uma categoria com o ID {id_categoria}.")
            return None
        finally:
            self.mongo.close()

        categoria = CategoriaAtividade(**dados)
        print("\nCategoria cadastrada com sucesso.")
        print(categoria.to_string())
        return categoria

    def atualizar_categoria(self) -> CategoriaAtividade | None:
        if not self.listar_categorias():
            return None

        id_categoria = self._ler_inteiro("\nInforme o ID da categoria que deseja alterar: ")
        documento = self._buscar_documento(id_categoria)
        if documento is None:
            print(f"A categoria com ID {id_categoria} não existe.")
            return None

        print("\nPressione Enter para manter o valor atual.")
        dados = self._ler_dados(documento)
        try:
            self.mongo.connect()
            resultado = self.mongo.db[self.COLLECTION_NAME].update_one(
                {"_id": documento["_id"]}, {"$set": dados}
            )
        finally:
            self.mongo.close()

        if not resultado.matched_count:
            print(f"A categoria com ID {id_categoria} não existe mais.")
            return None

        categoria = CategoriaAtividade(id_categoria=id_categoria, **dados)
        print("\nCategoria atualizada com sucesso.")
        print(categoria.to_string())
        return categoria

    def excluir_categoria(self) -> bool:
        if not self.listar_categorias():
            return False

        id_categoria = self._ler_inteiro("\nInforme o ID da categoria que deseja excluir: ")
        documento = self._buscar_documento(id_categoria)
        if documento is None:
            print(f"A categoria com ID {id_categoria} não existe.")
            return False

        return excluir_registro_seguro(
            self.COLLECTION_NAME, id_categoria, f"a categoria '{documento['nome_categoria']}'"
        )
