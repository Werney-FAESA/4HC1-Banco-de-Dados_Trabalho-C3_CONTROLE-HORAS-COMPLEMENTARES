# Registro de Uso de IA — Membro 1 (Kaike Vaccari do Nascimento)

Este arquivo registra o uso de IA como apoio ao desenvolvimento da camada de conexão MongoDB (`mongo_queries.py`), script de criação de coleções (`createCollectionsAndData.py`) e CRUD da coleção `cursos`, conforme a Observação (5) do edital da C3.

---

## Prompt #1

- **Data:** 24/11/2026
- **Fonte:** Google Antigravity (Gemini)
- **Prompt utilizado:**
  > "me diga o que eu "membro 1" preciso fazer nesse trabalho"
- **O que foi feito com a resposta:** Foi feito o levantamento das responsabilidades do Membro 1 no projeto (`src/conexion/mongo_queries.py`, `src/createCollectionsAndData.py`, `src/model/curso.py`, `src/controller/controller_curso.py`, `PROMPTS/PROMPTS_KAIKE.md` e commits em branch própria), identificando o que já possuía estrutura base e quais `# TODO` ainda precisavam ser implementados.

---

## Prompt #2

- **Data:** 24/11/2026
- **Fonte:** Google Antigravity (Gemini)
- **Prompt utilizado:**
  > "/plan Preciso saber como resolver os todos da classe controller_curso.py. Me ajude"
- **O que foi feito com a resposta:** Foi elaborado o plano de implementação dos métodos de `Controller_Curso` (`listar_cursos`, `verifica_existencia`, `inserir_curso`, `atualizar_curso` e `excluir_curso`), definindo o gerenciamento de conexão com `MongoQueries`, validações de entrada no console, exibição com `pandas.DataFrame` e integração com `excluir_registro_seguro`.

---

## Prompt #3

- **Data:** 24/11/2026
- **Fonte:** Google Antigravity (Gemini)
- **Prompt utilizado:**
  > "revise o #TODO em src/model/curso.py"
- **O que foi feito com a resposta:** A classe `Curso` em `src/model/curso.py` foi revisada (remoção do `# TODO`, adição de docstring e método `__str__` delegando para `to_string()`), foi corrigido o loop `while True:` em `_ler_texto` de `src/controller/controller_curso.py` e os testes unitários foram reexecutados com aprovação (`8/8`).

---

## Prompt #4

- **Data:** 24/11/2026
- **Fonte:** Google Antigravity (Gemini)
- **Prompt utilizado:**
  > "marque o que ja foi feito em tarefas faltantes"
- **O que foi feito com a resposta:** O script `src/createCollectionsAndData.py` foi executado para validar a recriação e carga inicial das 5 coleções no MongoDB e os 5 itens do Membro 1 em `TAREFAS_FALTANTES.md` foram marcados como concluídos (`[x]`).

---

## Prompt #5

- **Data:** 26/11/2026
- **Fonte:** Google Antigravity (Gemini)
- **Prompt utilizado:**
  > "o que ainda precisa ser feito por mim (membro 1)" / "complete o prompts.md"
- **O que foi feito com a resposta:** Foi verificado o estado da branch `main` após o merge do Pull Request #1 (`a2170f1`) e este arquivo (`PROMPTS/PROMPTS_KAIKE.md`) foi completado com o registro integral dos prompts utilizados pelo Membro 1, conforme a Observação (5) do edital da C3.
