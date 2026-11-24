"""Model da entidade ``categorias_atividade`` (Membro 3 - Bruno Mauro Bayer Laiber).

Campos na coleção ``categorias_atividade`` do MongoDB:
- ``id_categoria`` (int) - PK lógica
- ``nome_categoria`` (str) - Ex.: CURSO, EVENTO, PESQUISA
- ``limite_maximo_horas`` (int) - Ex.: 40, 15, 60
- ``descricao`` (str)
"""

from __future__ import annotations


class CategoriaAtividade:
    # TODO (Membro 3 - Bruno): Implementar construtor, getters, setters e to_string()
    def __init__(
        self,
        id_categoria: int | None = None,
        nome_categoria: str | None = None,
        limite_maximo_horas: int | None = None,
        descricao: str | None = None,
    ):
        self.set_id_categoria(id_categoria)
        self.set_nome_categoria(nome_categoria)
        self.set_limite_maximo_horas(limite_maximo_horas)
        self.set_descricao(descricao)

    def set_id_categoria(self, id_categoria: int | None):
        self.id_categoria = id_categoria

    def set_nome_categoria(self, nome_categoria: str | None):
        self.nome_categoria = nome_categoria

    def set_limite_maximo_horas(self, limite_maximo_horas: int | None):
        self.limite_maximo_horas = limite_maximo_horas

    def set_descricao(self, descricao: str | None):
        self.descricao = descricao

    def get_id_categoria(self) -> int | None:
        return self.id_categoria

    def get_nome_categoria(self) -> str | None:
        return self.nome_categoria

    def get_limite_maximo_horas(self) -> int | None:
        return self.limite_maximo_horas

    def get_descricao(self) -> str | None:
        return self.descricao

    def to_string(self) -> str:
        return (
            f"ID Categoria: {self.get_id_categoria()} | "
            f"Categoria: {self.get_nome_categoria()} | "
            f"Limite Máximo: {self.get_limite_maximo_horas()}h | "
            f"Descrição: {self.get_descricao()}"
        )
