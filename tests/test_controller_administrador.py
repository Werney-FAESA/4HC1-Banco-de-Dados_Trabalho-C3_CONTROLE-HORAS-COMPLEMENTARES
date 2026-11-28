"""Testes isolados do CRUD de administradores, sem servidor MongoDB."""

from __future__ import annotations

import builtins
import io
import sys
import unittest
from contextlib import redirect_stdout
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from controller.controller_administrador import Controller_Administrador


class _Cursor(list):
    def sort(self, campo, direcao):
        return _Cursor(
            sorted(
                self,
                key=lambda documento: documento[campo],
                reverse=direcao < 0,
            )
        )


class _Collection:
    def __init__(self, documentos=None):
        self.documentos = documentos or []

    def find(self, filtro, projecao):
        return _Cursor(deepcopy(self.documentos))

    def find_one(self, filtro, projecao=None):
        for documento in self.documentos:
            if all(documento.get(campo) == valor for campo, valor in filtro.items()):
                return deepcopy(documento)
        return None

    def insert_one(self, documento):
        self.documentos.append(deepcopy(documento))

    def update_one(self, filtro, atualizacao):
        for documento in self.documentos:
            if all(documento.get(campo) == valor for campo, valor in filtro.items()):
                documento.update(atualizacao["$set"])
                return


class _FakeMongo:
    def __init__(self):
        self.db = {
            "administradores": _Collection(
                [
                    {
                        "id_admin": 9002,
                        "nome_admin": "Secretaria",
                        "email": "secretaria@faesa.br",
                        "cargo": "Analista",
                    },
                    {
                        "id_admin": 9001,
                        "nome_admin": "Coordenador",
                        "email": "admin@faesa.br",
                        "cargo": "Coordenador",
                    },
                ]
            )
        }
        self.conexoes = 0
        self.fechamentos = 0

    def connect(self):
        self.conexoes += 1

    def close(self):
        self.fechamentos += 1


class ControllerAdministradorTest(unittest.TestCase):
    def setUp(self):
        self.controller = Controller_Administrador()
        self.mongo = _FakeMongo()
        self.controller.mongo = self.mongo

    def _executar_com_entradas(self, entradas, funcao):
        with patch.object(builtins, "input", side_effect=entradas), redirect_stdout(
            io.StringIO()
        ):
            return funcao()

    def test_listar_administradores_ordena_e_fecha_conexao(self):
        with redirect_stdout(io.StringIO()) as saida:
            resultado = self.controller.listar_administradores()

        texto = saida.getvalue()
        self.assertTrue(resultado)
        self.assertLess(texto.index("9001"), texto.index("9002"))
        self.assertEqual(self.mongo.conexoes, self.mongo.fechamentos)

    def test_inserir_administrador_valida_id_e_salva_documento(self):
        resultado = self._executar_com_entradas(
            ["0", "invalido", "9003", "Daniel", "daniel@faesa.br", "Coordenador"],
            self.controller.inserir_administrador,
        )

        self.assertEqual(resultado.get_id_admin(), 9003)
        self.assertEqual(
            self.mongo.db["administradores"].documentos[-1],
            {
                "id_admin": 9003,
                "nome_admin": "Daniel",
                "email": "daniel@faesa.br",
                "cargo": "Coordenador",
            },
        )
        self.assertEqual(self.mongo.conexoes, self.mongo.fechamentos)

    def test_inserir_administrador_rejeita_email_duplicado(self):
        resultado = self._executar_com_entradas(
            ["9003", "Outro Administrador", "admin@faesa.br"],
            self.controller.inserir_administrador,
        )

        self.assertIsNone(resultado)
        self.assertEqual(len(self.mongo.db["administradores"].documentos), 2)

    def test_atualizar_administrador_preserva_campos_vazios(self):
        resultado = self._executar_com_entradas(
            ["9001", "Coordenador Atualizado", "", ""],
            self.controller.atualizar_administrador,
        )

        documento = self.mongo.db["administradores"].documentos[1]
        self.assertEqual(resultado.get_nome_admin(), "Coordenador Atualizado")
        self.assertEqual(documento["email"], "admin@faesa.br")
        self.assertEqual(documento["cargo"], "Coordenador")

    def test_atualizar_administrador_rejeita_email_em_uso(self):
        resultado = self._executar_com_entradas(
            ["9001", "Coordenador", "secretaria@faesa.br"],
            self.controller.atualizar_administrador,
        )

        self.assertIsNone(resultado)
        self.assertEqual(
            self.mongo.db["administradores"].documentos[1]["email"],
            "admin@faesa.br",
        )

    def test_excluir_administrador_delega_para_exclusao_segura(self):
        with patch(
            "controller.controller_administrador.excluir_registro_seguro",
            return_value=True,
        ) as excluir:
            resultado = self._executar_com_entradas(
                ["9001"], self.controller.excluir_administrador
            )

        self.assertTrue(resultado)
        excluir.assert_called_once_with(
            "administradores", 9001, "o administrador 'Coordenador'"
        )


if __name__ == "__main__":
    unittest.main()
