"""Model da entidade ``cursos`` (Membro 1 - Kaike Vaccari do Nascimento).

Campos na coleção ``cursos`` do MongoDB:
- ``id_curso`` (int) - PK lógica
- ``nome_curso`` (str)
- ``horas_exigidas`` (int)
- ``coordenador`` (str)
"""

from __future__ import annotations


class Curso:
    """Representa um documento da coleção ``cursos`` do MongoDB."""

    def __init__(
        self,
        id_curso: int | None = None,
        nome_curso: str | None = None,
        horas_exigidas: int | None = None,
        coordenador: str | None = None,
    ):
        self.set_id_curso(id_curso)
        self.set_nome_curso(nome_curso)
        self.set_horas_exigidas(horas_exigidas)
        self.set_coordenador(coordenador)

    def set_id_curso(self, id_curso: int | None):
        self.id_curso = id_curso

    def set_nome_curso(self, nome_curso: str | None):
        self.nome_curso = nome_curso

    def set_horas_exigidas(self, horas_exigidas: int | None):
        self.horas_exigidas = horas_exigidas

    def set_coordenador(self, coordenador: str | None):
        self.coordenador = coordenador

    def get_id_curso(self) -> int | None:
        return self.id_curso

    def get_nome_curso(self) -> str | None:
        return self.nome_curso

    def get_horas_exigidas(self) -> int | None:
        return self.horas_exigidas

    def get_coordenador(self) -> str | None:
        return self.coordenador

    def to_string(self) -> str:
        return (
            f"ID Curso: {self.get_id_curso()} | "
            f"Curso: {self.get_nome_curso()} | "
            f"Horas Exigidas: {self.get_horas_exigidas()}h | "
            f"Coordenador: {self.get_coordenador()}"
        )

    def __str__(self) -> str:
        return self.to_string()
