# LISTA DE MEMBROS E TAREFAS — TRABALHO C3 (MONGODB)
### Lista o nome de cada membro do grupo e suas responsabilidades no Sistema de Controle de Horas Complementares.

* **Membro 1 - Kaike Vaccari do Nascimento**
  * **Foco:** Conexão MongoDB (`src/conexion/mongo_queries.py`), script de criação e carga inicial das coleções (`src/createCollectionsAndData.py`) e CRUD da coleção `cursos` (`src/model/curso.py`, `src/controller/controller_curso.py`).
* **Membro 2 - Issacar Mattos Gutler**
  * **Foco:** CRUD da coleção `alunos` (`src/model/aluno.py`, `src/controller/controller_aluno.py`), garantindo associação com instância de `Curso` e validação de `id_curso` existente no MongoDB.
* **Membro 3 - Bruno Mauro Bayer Laiber**
  * **Foco:** CRUD da coleção `categorias_atividade` (`src/model/categoria_atividade.py`, `src/controller/controller_categoria_atividade.py`) e módulo de Exclusão Segura com trava de integridade referencial entre coleções (`src/utils/exclusao_segura.py` — item 7.c.5.i do edital).
* **Membro 4 - Daniel Lima Del'Antonio**
  * **Foco:** CRUD da coleção `administradores` (`src/model/administrador.py`, `src/controller/controller_administrador.py`) e Módulo de Relatórios com Aggregation Pipeline do MongoDB (`src/reports/relatorios.py` — consultas com `$group` e `$lookup` — itens 7.a.1.i e 7.a.1.ii do edital).
* **Membro 5 - Werney Ferreira Rocha**
  * **Foco:** Menu Principal e fluxo contínuo (`src/principal.py`), configurações e contagem de documentos (`src/utils/config.py`), Splash Screen (`src/utils/splash_screen.py`), Docker MongoDB (`docker-compose.yml`), Diagramas Mermaid unificados (`diagramas/`), documentação Linux (`README.md`) e vídeo demonstrativo no YouTube.
* **Membro 6 - Gabriel Antônio Galdino dos Santos**
  * **Foco:** CRUD da coleção `tickets_atividades` (`src/model/ticket_atividade.py`, `src/controller/controller_ticket_atividade.py`), validações cruzadas das referências (`matricula_aluno`, `id_categoria`, `id_admin_avaliador`) e validação do limite máximo de horas por categoria.
