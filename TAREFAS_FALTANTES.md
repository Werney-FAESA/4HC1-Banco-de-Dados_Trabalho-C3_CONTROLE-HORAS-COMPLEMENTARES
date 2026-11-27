# Checklist de Tarefas por Membro — Trabalho C3 (MongoDB)

> Marque com `[x]` à medida que cada integrante concluir e abrir o Pull Request da sua branch.

---

## 👤 Membro 1 — Kaike Vaccari do Nascimento (Conexão, Seed & `cursos`)

- [x] **Revisar e testar `src/conexion/mongo_queries.py`**:
  - Validar conexão com o container MongoDB (`localhost:27017`, banco `labdatabase`).
- [x] **Completar e testar `src/createCollectionsAndData.py`**:
  - Criar as 5 coleções (`cursos`, `alunos`, `categorias_atividade`, `administradores`, `tickets_atividades`) e popular com os dados iniciais.
- [x] **Implementar `src/model/curso.py`**:
  - Classe `Curso` com construtor `__init__`, atributos (`id_curso`, `nome_curso`, `horas_exigidas`, `coordenador`), getters, setters e `to_string()`.
- [x] **Implementar `src/controller/controller_curso.py`**:
  - Métodos `inserir_curso()`, `atualizar_curso()`, `excluir_curso()`, `listar_cursos()` e `verifica_existencia()` usando `MongoQueries`.
- [x] **Registrar prompts em `PROMPTS/PROMPTS_KAIKE.md`**.

---

## 👤 Membro 2 — Issacar Mattos Gutler (Coleção `alunos`)

- [x] **Implementar `src/model/aluno.py`**:
  - Classe `Aluno` com atributos (`matricula`, `nome_aluno`, `email`, `periodo`, `curso: Curso`), getters, setters e `to_string()`.
- [x] **Implementar `src/controller/controller_aluno.py`**:
  - Métodos `inserir_aluno()`, `atualizar_aluno()`, `excluir_aluno()`, `listar_alunos()` e `verifica_existencia()` com validação de `id_curso` na coleção `cursos` e exclusão via `excluir_registro_seguro`.
- [x] **Registrar prompts em `PROMPTS/PROMPTS_ISSACAR.md`**.

---

## 👤 Membro 3 — Bruno Mauro Bayer Laiber (Coleção `categorias_atividade` & Exclusão Segura)

- [x] **Implementar `src/model/categoria_atividade.py`**:
  - Classe `CategoriaAtividade` com atributos (`id_categoria`, `nome_categoria`, `limite_maximo_horas`, `descricao`), getters, setters e `to_string()`.
- [x] **Implementar `src/controller/controller_categoria_atividade.py`**:
  - Métodos `inserir_categoria()`, `atualizar_categoria()`, `excluir_categoria()`, `listar_categorias()` e `verifica_existencia()`.
- [x] **Implementar `src/utils/exclusao_segura.py` para MongoDB (item 7.c.5.i do edital)**:
  - Mapa `DEPENDENCIAS` das 5 coleções, contagem de documentos filhos (`count_documents`) e opção de exclusão recursiva em cascata (`delete_many` / `delete_one`).
- [x] **Registrar prompts em `PROMPTS/PROMPTS_BRUNO.md`**.

---

## 👤 Membro 4 — Daniel Lima Del'Antonio (Coleção `administradores` & Relatórios MongoDB)

- [ ] **Implementar `src/model/administrador.py`**:
  - Classe `Administrador` com atributos (`id_admin`, `nome_admin`, `email`, `cargo`), getters, setters e `to_string()`.
- [ ] **Implementar `src/controller/controller_administrador.py`**:
  - Métodos `inserir_administrador()`, `atualizar_administrador()`, `excluir_administrador()`, `listar_administradores()` e `verifica_existencia()`.
- [ ] **Implementar `src/reports/relatorios.py`**:
  - Relatórios com `$group` (sumarização de horas por aluno, por categoria e por status) e relatórios com `$lookup` (junção de tickets detalhados e alunos com cursos).
- [ ] **Registrar prompts em `PROMPTS/PROMPTS_DANIEL.md`**.

---

## 👤 Membro 5 — Werney Ferreira Rocha (Menu Principal, Splash Screen, Docker, Diagramas, README & Vídeo)

- [x] **Criar `src/utils/config.py`, `src/utils/splash_screen.py` e `src/principal.py`**.
- [x] **Configurar `docker-compose.yml` para o MongoDB e `requirements.txt`**.
- [x] **Criar os diagramas Mermaid em `diagramas/diagrama_logico.mmd` e `diagramas/diagrama_ER.mmd`**.
- [ ] **Exportar imagem `.png` / `.pdf` do diagrama lógico em `diagramas/`**.
- [ ] **Validar integração final de todos os controllers e relatórios no `README.md`**.
- [ ] **Gravar o Vídeo Demonstrativo no YouTube e colocar o link no `README.md`**.
- [ ] **Adicionar `howardroatti` como colaborador no repositório GitHub e postar o link no AVA até 04/12/2026**.

---

## 👤 Membro 6 — Gabriel Antônio Galdino dos Santos (Coleção `tickets_atividades`)

- [ ] **Implementar `src/model/ticket_atividade.py`**:
  - Classe `TicketAtividade` com atributos (`id_ticket`, `titulo`, `horas_solicitadas`, `horas_validadas`, `status`, `observacao_admin`, `aluno: Aluno`, `categoria: CategoriaAtividade`, `admin_avaliador: Administrador`), getters, setters e `to_string()`.
- [ ] **Implementar `src/controller/controller_ticket_atividade.py`**:
  - Métodos `inserir_ticket()`, `atualizar_ticket()`, `excluir_ticket()`, `listar_tickets()` e `verifica_existencia()` validando aluno, categoria, administrador e limite máximo de horas da categoria.
- [ ] **Registrar prompts em `PROMPTS/PROMPTS_GABRIEL.md`**.
