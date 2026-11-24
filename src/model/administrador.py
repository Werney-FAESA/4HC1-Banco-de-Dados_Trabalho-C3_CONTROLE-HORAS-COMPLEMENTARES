"""Model da entidade ``administradores`` (Membro 4 - Daniel Lima Del'Antonio).

Campos na coleção ``administradores`` do MongoDB:
- ``id_admin`` (int) - PK lógica
- ``nome_admin`` (str)
- ``email`` (str)
- ``cargo`` (str)
"""

from __future__ import annotations


class Administrador:
    # TODO (Membro 4 - Daniel): Implementar construtor, getters, setters e to_string()
    def __init__(
        self,
        id_admin: int | None = None,
        nome_admin: str | None = None,
        email: str | None = None,
        cargo: str | None = None,
    ):
        self.set_id_admin(id_admin)
        self.set_nome_admin(nome_admin)
        self.set_email(email)
        self.set_cargo(cargo)

    def set_id_admin(self, id_admin: int | None):
        self.id_admin = id_admin

    def set_nome_admin(self, nome_admin: str | None):
        self.nome_admin = nome_admin

    def set_email(self, email: str | None):
        self.email = email

    def set_cargo(self, cargo: str | None):
        self.cargo = cargo

    def get_id_admin(self) -> int | None:
        return self.id_admin

    def get_nome_admin(self) -> str | None:
        return self.nome_admin

    def get_email(self) -> str | None:
        return self.email

    def get_cargo(self) -> str | None:
        return self.cargo

    def to_string(self) -> str:
        return (
            f"ID Admin: {self.get_id_admin()} | "
            f"Nome: {self.get_nome_admin()} | "
            f"E-mail: {self.get_email()} | "
            f"Cargo: {self.get_cargo()}"
        )
