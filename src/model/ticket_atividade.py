"""Model da entidade ``tickets_atividades`` (Membro 6 - Gabriel Antônio Galdino dos Santos).

Campos na coleção ``tickets_atividades`` do MongoDB:
- ``id_ticket`` (int) - PK lógica
- ``matricula_aluno`` (int) - FK lógica para ``alunos.matricula``
- ``id_categoria`` (int) - FK lógica para ``categorias_atividade.id_categoria``
- ``id_admin_avaliador`` (int | None) - FK lógica para ``administradores.id_admin``
- ``titulo`` (str)
- ``horas_solicitadas`` (int)
- ``horas_validadas`` (int)
- ``status`` (str) - PENDENTE, APROVADO, RECUSADO
- ``observacao_admin`` (str)

Observação do Edital (Etapa 2):
Armazena as instâncias associadas `aluno: Aluno`, `categoria: CategoriaAtividade`
e `admin_avaliador: Administrador | None`.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.administrador import Administrador
    from model.aluno import Aluno
    from model.categoria_atividade import CategoriaAtividade


class TicketAtividade:
    # TODO (Membro 6 - Gabriel): Revisar/completar construtor, getters, setters e to_string()
    def __init__(
        self,
        id_ticket: int | None = None,
        titulo: str | None = None,
        horas_solicitadas: int | None = None,
        horas_validadas: int | None = None,
        status: str | None = "PENDENTE",
        observacao_admin: str | None = None,
        aluno: Aluno | None = None,
        categoria: CategoriaAtividade | None = None,
        admin_avaliador: Administrador | None = None,
    ):
        self.set_id_ticket(id_ticket)
        self.set_titulo(titulo)
        self.set_horas_solicitadas(horas_solicitadas)
        self.set_horas_validadas(horas_validadas)
        self.set_status(status)
        self.set_observacao_admin(observacao_admin)
        self.set_aluno(aluno)
        self.set_categoria(categoria)
        self.set_admin_avaliador(admin_avaliador)

    def set_id_ticket(self, id_ticket: int | None):
        self.id_ticket = id_ticket

    def set_titulo(self, titulo: str | None):
        self.titulo = titulo

    def set_horas_solicitadas(self, horas_solicitadas: int | None):
        self.horas_solicitadas = horas_solicitadas

    def set_horas_validadas(self, horas_validadas: int | None):
        self.horas_validadas = horas_validadas

    def set_status(self, status: str | None):
        self.status = status

    def set_observacao_admin(self, observacao_admin: str | None):
        self.observacao_admin = observacao_admin

    def set_aluno(self, aluno: Aluno | None):
        self.aluno = aluno

    def set_categoria(self, categoria: CategoriaAtividade | None):
        self.categoria = categoria

    def set_admin_avaliador(self, admin_avaliador: Administrador | None):
        self.admin_avaliador = admin_avaliador

    def get_id_ticket(self) -> int | None:
        return self.id_ticket

    def get_titulo(self) -> str | None:
        return self.titulo

    def get_horas_solicitadas(self) -> int | None:
        return self.horas_solicitadas

    def get_horas_validadas(self) -> int | None:
        return self.horas_validadas

    def get_status(self) -> str | None:
        return self.status

    def get_observacao_admin(self) -> str | None:
        return self.observacao_admin

    def get_aluno(self) -> Aluno | None:
        return self.aluno

    def get_categoria(self) -> CategoriaAtividade | None:
        return self.categoria

    def get_admin_avaliador(self) -> Administrador | None:
        return self.admin_avaliador

    def to_string(self) -> str:
        aluno = self.get_aluno()
        categoria = self.get_categoria()
        admin = self.get_admin_avaliador()
        nome_aluno = f"{aluno.get_nome_aluno()} ({aluno.get_matricula()})" if aluno else "N/A"
        nome_cat = categoria.get_nome_categoria() if categoria else "N/A"
        nome_admin = admin.get_nome_admin() if admin else "Não avaliado"
        return (
            f"Ticket #{self.get_id_ticket()} | "
            f"Aluno: {nome_aluno} | "
            f"Categoria: {nome_cat} | "
            f"Título: {self.get_titulo()} | "
            f"Horas (Solic./Valid.): {self.get_horas_solicitadas()}h / {self.get_horas_validadas()}h | "
            f"Status: {self.get_status()} | "
            f"Avaliador: {nome_admin} | "
            f"Obs.: {self.get_observacao_admin()}"
        )
