"""Testes isolados do CRUD de alunos, sem depender de um servidor MongoDB."""

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

from controller.controller_aluno import Controller_Aluno
from model.aluno import Aluno
from model.curso import Curso


class _Cursor(list):
    def sort(self, campo, direcao):
        return _Cursor(sorted(self, key=lambda documento: documento[campo], reverse=direcao < 0))


class _Collection:
    def __init__(self, documentos=None, resultado_aggregate=None):
        self.documentos = documentos or []
        self.resultado_aggregate = resultado_aggregate
        self.pipeline = None

    def find(self, filtro, projecao):
        return _Cursor(deepcopy(self.documentos))

    def find_one(self, filtro, projecao=None):
        for documento in self.documentos:
            if all(documento.get(campo) == valor for campo, valor in filtro.items()):
                return deepcopy(documento)
        return None

    def aggregate(self, pipeline):
        self.pipeline = pipeline
        if self.resultado_aggregate is not None:
            return deepcopy(self.resultado_aggregate)

        cursos = {curso["id_curso"]: curso for curso in self.db["cursos"].documentos}
        return [
            {
                **deepcopy(aluno),
                "nome_curso": cursos.get(aluno["id_curso"], {}).get("nome_curso"),
            }
            for aluno in sorted(self.documentos, key=lambda documento: documento["matricula"])
        ]

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
            "alunos": _Collection(
                [{"matricula": 202601, "nome_aluno": "Ana", "email": "ana@faesa.br", "periodo": 4, "id_curso": 1}]
            ),
            "cursos": _Collection(
                [
                    {"id_curso": 1, "nome_curso": "Sistemas de Informação", "horas_exigidas": 120, "coordenador": "Prof. A"},
                    {"id_curso": 2, "nome_curso": "Ciência da Computação", "horas_exigidas": 160, "coordenador": "Prof. B"},
                ]
            ),
        }
        for colecao in self.db.values():
            colecao.db = self.db
        self.conexoes = 0
        self.fechamentos = 0

    def connect(self):
        self.conexoes += 1

    def close(self):
        self.fechamentos += 1


class ControllerAlunoTest(unittest.TestCase):
    def setUp(self):
        self.controller = Controller_Aluno()
        self.mongo = _FakeMongo()
        self.controller.mongo = self.mongo

    def _executar_com_entradas(self, entradas, funcao):
        with patch.object(builtins, "input", side_effect=entradas), redirect_stdout(io.StringIO()):
            return funcao()

    def test_model_mantem_associacao_com_curso(self):
        aluno = Aluno(202601, "Ana", "ana@faesa.br", 4, Curso(1, "SI", 120, "Prof. A"))
        self.assertEqual(aluno.get_curso().get_nome_curso(), "SI")
        self.assertIn("Curso: SI", aluno.to_string())

    def test_listar_alunos_usa_lookup_e_exibe_curso(self):
        with redirect_stdout(io.StringIO()) as saida:
            resultado = self.controller.listar_alunos()

        pipeline = self.mongo.db["alunos"].pipeline
        self.assertTrue(resultado)
        self.assertEqual(pipeline[0]["$lookup"]["from"], "cursos")
        self.assertEqual(pipeline[-1]["$sort"], {"matricula": 1})
        self.assertIn("Sistemas de Informação", saida.getvalue())

    def test_inserir_aluno_valida_matricula_duplicada(self):
        resultado = self._executar_com_entradas(["202601"], self.controller.inserir_aluno)
        self.assertIsNone(resultado)
        self.assertEqual(len(self.mongo.db["alunos"].documentos), 1)

    def test_inserir_aluno_valida_curso_e_cria_associacao(self):
        resultado = self._executar_com_entradas(
            ["202602", "Beatriz", "bia@faesa.br", "2", "2"],
            self.controller.inserir_aluno,
        )
        self.assertEqual(resultado.get_matricula(), 202602)
        self.assertEqual(resultado.get_curso().get_id_curso(), 2)
        self.assertEqual(self.mongo.db["alunos"].documentos[-1]["id_curso"], 2)

    def test_inserir_aluno_rejeita_curso_inexistente(self):
        resultado = self._executar_com_entradas(
            ["202602", "Beatriz", "bia@faesa.br", "2", "999"],
            self.controller.inserir_aluno,
        )
        self.assertIsNone(resultado)
        self.assertEqual(len(self.mongo.db["alunos"].documentos), 1)

    def test_atualizar_aluno_usa_update_one_e_mantem_valores_com_enter(self):
        resultado = self._executar_com_entradas(
            ["202601", "Ana Atualizada", "", "5", "2"],
            self.controller.atualizar_aluno,
        )
        documento = self.mongo.db["alunos"].documentos[0]
        self.assertEqual(resultado.get_curso().get_nome_curso(), "Ciência da Computação")
        self.assertEqual(documento["nome_aluno"], "Ana Atualizada")
        self.assertEqual(documento["email"], "ana@faesa.br")
        self.assertEqual(documento["periodo"], 5)
        self.assertEqual(documento["id_curso"], 2)

    def test_excluir_aluno_delega_para_exclusao_segura(self):
        with patch("controller.controller_aluno.excluir_registro_seguro", return_value=True) as excluir:
            resultado = self._executar_com_entradas(["202601"], self.controller.excluir_aluno)

        self.assertTrue(resultado)
        excluir.assert_called_once_with("alunos", 202601, "o aluno 'Ana'")


if __name__ == "__main__":
    unittest.main()
