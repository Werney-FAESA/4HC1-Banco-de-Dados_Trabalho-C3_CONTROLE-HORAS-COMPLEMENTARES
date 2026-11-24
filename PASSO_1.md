# 🚀 Guia Rápido de Branches e Commits por Membro (Trabalho C3 - MongoDB)

> **Importante (Edital C3, Página 7, Obs. 1):**  
> *"A participação de cada membro será medida pelo número de commits no repositório GitHub do trabalho; o(a) aluno(a) que não registrar commits (contribuição efetiva) terá sua avaliação individual zerada automaticamente."*

---

## 📌 Fluxo Git para Todos os 6 Integrantes

1. **Clonar o repositório e atualizar a branch principal:**
   ```bash
   git clone https://github.com/Werney-FAESA/4HC1-Banco-de-Dados_Trabalho-C3_CONTROLE-HORAS-COMPLEMENTARES.git
   cd 4HC1-Banco-de-Dados_Trabalho-C3_CONTROLE-HORAS-COMPLEMENTARES
   git pull origin main
   ```
2. **Criar a sua branch individual:**
   ```bash
   git checkout -b c3-membro-X-seu-nome
   ```
3. **Implementar os arquivos sob sua responsabilidade (faça 2 a 4 commits separados para registrar bem seu histórico no GitHub):**
   - Commit 1: `model` da sua entidade (ou diagrama/conexão)
   - Commit 2: `controller` da sua entidade (inserir, listar, atualizar, excluir)
   - Commit 3: módulo extra (`exclusao_segura.py`, `relatorios.py`, `createCollectionsAndData.py`, etc.) e atualização do seu arquivo em `PROMPTS/`
4. **Enviar a branch e abrir o Pull Request:**
   ```bash
   git add .
   git commit -m "feat(c3): implementa modulo do membro X"
   git push -u origin c3-membro-X-seu-nome
   ```

---

## 🗂️ Resumo dos Arquivos de Cada Membro

| Membro | Nome | Branch Sugerida | Arquivos Principais para Commitar |
| :--- | :--- | :--- | :--- |
| **Membro 1** | Kaike Vaccari | `c3-membro1-kaike-cursos-conexao` | `src/conexion/mongo_queries.py`<br>`src/createCollectionsAndData.py`<br>`src/model/curso.py`<br>`src/controller/controller_curso.py`<br>`PROMPTS/PROMPTS_KAIKE.md` |
| **Membro 2** | Issacar Gutler | `c3-membro2-issacar-alunos` | `src/model/aluno.py`<br>`src/controller/controller_aluno.py`<br>`PROMPTS/PROMPTS_ISSACAR.md` |
| **Membro 3** | Bruno Laiber | `c3-membro3-bruno-categorias-fk` | `src/model/categoria_atividade.py`<br>`src/controller/controller_categoria_atividade.py`<br>`src/utils/exclusao_segura.py`<br>`PROMPTS/PROMPTS_BRUNO.md` |
| **Membro 4** | Daniel Del'Antonio | `c3-membro4-daniel-admin-relatorios` | `src/model/administrador.py`<br>`src/controller/controller_administrador.py`<br>`src/reports/relatorios.py`<br>`PROMPTS/PROMPTS_DANIEL.md` |
| **Membro 5** | Werney Rocha | `c3-membro5-werney-menus-integracao` | `src/principal.py`<br>`src/utils/config.py`<br>`src/utils/splash_screen.py`<br>`diagramas/diagrama_logico.mmd`<br>`diagramas/diagrama_ER.mmd`<br>`docker-compose.yml` & `README.md`<br>`PROMPTS/PROMPTS_WERNEY.md` |
| **Membro 6** | Gabriel Galdino | `c3-membro6-gabriel-tickets` | `src/model/ticket_atividade.py`<br>`src/controller/controller_ticket_atividade.py`<br>`PROMPTS/PROMPTS_GABRIEL.md` |
