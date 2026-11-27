"""Model da entidade ``alunos`` (Membro 2 - Issacar Mattos Gutler).

Campos na coleção ``alunos`` do MongoDB:
- ``matricula`` (int) - PK lógica
- ``nome_aluno`` (str)
- ``email`` (str)
- ``periodo`` (int)
- ``id_curso`` (int) - FK lógica para ``cursos.id_curso``

Observação do Edital (Etapa 2):
Sempre que um objeto possui uma associação com outro, a classe deverá ter como
atributo uma instância do outro objeto (`curso: Curso`), não apenas seu ID.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.curso import Curso


class Aluno:
    """Representa um documento da coleção ``alunos`` com seu curso associado."""
    def __init__(
        self,
        matricula: int | None = None,
        nome_aluno: str | None = None,
        email: str | None = None,
        periodo: int | None = None,
        curso: Curso | None = None,
    ):
        self.set_matricula(matricula)
        self.set_nome_aluno(nome_aluno)
        self.set_email(email)
        self.set_periodo(periodo)
        self.set_curso(curso)

    def set_matricula(self, matricula: int | None):
        self.matricula = matricula

    def set_nome_aluno(self, nome_aluno: str | None):
        self.nome_aluno = nome_aluno

    def set_email(self, email: str | None):
        self.email = email

    def set_periodo(self, periodo: int | None):
        self.periodo = periodo

    def set_curso(self, curso: Curso | None):
        self.curso = curso

    def get_matricula(self) -> int | None:
        return self.matricula

    def get_nome_aluno(self) -> str | None:
        return self.nome_aluno

    def get_email(self) -> str | None:
        return self.email

    def get_periodo(self) -> int | None:
        return self.periodo

    def get_curso(self) -> Curso | None:
        return self.curso

    def to_string(self) -> str:
        curso = self.get_curso()
        nome_curso = curso.get_nome_curso() if curso else "N/A"
        return (
            f"Matrícula: {self.get_matricula()} | "
            f"Aluno: {self.get_nome_aluno()} | "
            f"E-mail: {self.get_email()} | "
            f"Período: {self.get_periodo()}º | "
            f"Curso: {nome_curso}"
        )
