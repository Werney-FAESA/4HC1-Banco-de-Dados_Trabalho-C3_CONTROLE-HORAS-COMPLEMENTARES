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
