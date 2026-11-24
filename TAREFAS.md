# 👥 Divisão de Trabalho da Equipe (6 Integrantes) — Controle de Horas Complementares (C3 MongoDB)

> **Disciplina:** Banco de Dados — FAESA (2026/2) | **Professor:** Prof. M.Sc. Howard Roatti  
> **Tema:** Sistema de Controle de Horas Complementares  
> **Banco de Dados:** MongoDB (NoSQL) via Docker / VM LabDatabase (`pymongo` + `pandas`, sem ODM/ORM)  
> **Data de Entrega no AVA:** 04/12/2026  

---

## ⚠️ Regras Críticas do Edital da C3

1. **Commits Obrigatórios no GitHub (Obs. 1, pág. 7):** A participação de cada integrante será medida pelo **número de commits no repositório GitHub**. Quem não tiver commits registrados terá a nota individual **zerada automaticamente**.
2. **Professor como Colaborador (Obs. 6, pág. 7):** Adicionar o usuário **`howardroatti`** como colaborador no repositório GitHub do grupo.
3. **Transparência no Uso de IA (Obs. 5, pág. 7):** Todo prompt utilizado deve ser registrado na pasta `PROMPTS/` (arquivo `PROMPTS_<NOME>.md`), contendo o prompt, a ferramenta utilizada e o que foi feito com a resposta.
4. **Projeto Novo no MongoDB (Item 5, pág. 2-3):** Como mudamos o tema da C2 (Pokédex) para **Controle de Horas Complementares**, seguimos o **Item 5** do edital: o script `src/createCollectionsAndData.py` conecta diretamente ao **MongoDB**, cria as 5 coleções do diagrama relacional e insere os documentos iniciais.

---

## 📌 Quadro Resumo de Responsabilidades

| Integrante | Nome | Papel Principal | Coleções / Módulos em Foco | Entregáveis Específicos |
| :--- | :--- | :--- | :--- | :--- |
| **Membro 1** | Kaike Vaccari do Nascimento | Arquiteto NoSQL & Backend | `cursos` + Conexão MongoDB & Seed | `mongo_queries.py`, `createCollectionsAndData.py`, `model/curso.py`, `controller_curso.py` |
| **Membro 2** | Issacar Mattos Gutler | Desenvolvedor Backend | `alunos` | `model/aluno.py`, `controller_aluno.py` |
| **Membro 3** | Bruno Mauro Bayer Laiber | Desenvolvedor Backend & Integridade | `categorias_atividade` + Trava de FK | `model/categoria_atividade.py`, `controller_categoria_atividade.py`, `utils/exclusao_segura.py` |
| **Membro 4** | Daniel Lima Del'Antonio | Especialista em Aggregation & Backend | `administradores` + Relatórios (`$group` e `$lookup`) | `model/administrador.py`, `controller_administrador.py`, `reports/relatorios.py` |
| **Membro 5** | Werney Ferreira Rocha | Líder de Integração, Menus & QA | Menu Principal, Splash Screen, Diagramas, Docker & Vídeo | `principal.py`, `config.py`, `splash_screen.py`, `docker-compose.yml`, `diagramas/`, `README.md` |
| **Membro 6** | Gabriel Antônio Galdino dos Santos | Desenvolvedor Backend & Regras | `tickets_atividades` + Validação de Horas | `model/ticket_atividade.py`, `controller_ticket_atividade.py` |

---

## 🗄️ Padrão Oficial das 5 Coleções no MongoDB (Nomes de Campos)

Para que os controllers, relatórios (`$lookup` / `$group`) e a exclusão segura funcionem juntos sem conflito, **todos os membros devem respeitar exatamente estes nomes de coleções e chaves JSON**:

### 1. Coleção `cursos` (Membro 1 — Kaike)
```json
{
  "id_curso": 1,
  "nome_curso": "Ciencia da Computacao",
  "horas_exigidas": 120,
  "coordenador": "Prof. Howard Roatti"
}
```
* **PK lógica:** `id_curso` (`int`)
* **Dependentes (FKs que apontam para cá):** `alunos.id_curso`

### 2. Coleção `alunos` (Membro 2 — Issacar)
```json
{
  "matricula": 202601,
  "nome_aluno": "Werney Ferreira Rocha",
  "email": "werney@faesa.br",
  "periodo": 4,
  "id_curso": 1
}
```
* **PK lógica:** `matricula` (`int`)
* **FK lógica:** `id_curso` (`int`) → referencia `cursos.id_curso`
* **Dependentes (FKs que apontam para cá):** `tickets_atividades.matricula_aluno`

### 3. Coleção `categorias_atividade` (Membro 3 — Bruno)
```json
{
  "id_categoria": 1,
  "nome_categoria": "CURSO",
  "limite_maximo_horas": 40,
  "descricao": "Cursos livres, bootcamps e certificacoes"
}
```
* **PK lógica:** `id_categoria` (`int`)
* **Categorias iniciais do sistema:**
  * `1` — `CURSO` (limite: `40` horas)
  * `2` — `EVENTO` (limite: `15` horas)
  * `3` — `PESQUISA` (limite: `60` horas)
* **Dependentes (FKs que apontam para cá):** `tickets_atividades.id_categoria`

### 4. Coleção `administradores` (Membro 4 — Daniel)
```json
{
  "id_admin": 9001,
  "nome_admin": "Coordenador FAESA",
  "email": "admin@faesa.br",
  "cargo": "Coordenador de Curso"
}
```
* **PK lógica:** `id_admin` (`int`)
* **Dependentes (FKs que apontam para cá):** `tickets_atividades.id_admin_avaliador`

### 5. Coleção `tickets_atividades` (Membro 6 — Gabriel)
```json
{
  "id_ticket": 1,
  "matricula_aluno": 202601,
  "id_categoria": 1,
  "id_admin_avaliador": 9001,
  "titulo": "Curso de Java POO",
  "horas_solicitadas": 20,
  "horas_validadas": 20,
  "status": "APROVADO",
  "observacao_admin": "Certificado validado"
}
```
* **PK lógica:** `id_ticket` (`int`)
* **FKs lógicas:**
  * `matricula_aluno` (`int`) → referencia `alunos.matricula`
  * `id_categoria` (`int`) → referencia `categorias_atividade.id_categoria`
  * `id_admin_avaliador` (`int` ou `None`) → referencia `administradores.id_admin`
* **Valores válidos de `status`:** `"PENDENTE"`, `"APROVADO"`, `"RECUSADO"`

---

## 🔍 Detalhamento das Tarefas por Integrante

---

### 👤 Membro 1 (Kaike): Conexão MongoDB, Criação de Coleções e CRUD de `cursos`

1. **Módulo de Conexão (`src/conexion/mongo_queries.py`)**:
   - Conectar ao MongoDB sem ODM/ORM usando `pymongo.MongoClient`.
   - Ler credenciais de `src/conexion/passphrase/authentication.mongo` ou variáveis de ambiente (`MONGO_HOST`, `MONGO_PORT`, `MONGO_DB`, `MONGO_USER`, `MONGO_PASSWORD`), suportando tanto MongoDB sem autenticação (padrão da VM LabDatabase `mongodb://localhost:27017/`) quanto autenticado.
2. **Script de Criação e Carga Inicial (`src/createCollectionsAndData.py`)**:
   - Implementar `createCollections(drop_if_exists=True)` criando as 5 coleções: `cursos`, `alunos`, `categorias_atividade`, `administradores`, `tickets_atividades`.
   - Inserir os documentos iniciais baseados nos dados do projeto de Horas Complementares (`insert_many`).
3. **Model e Controller de Curso (`src/model/curso.py` e `src/controller/controller_curso.py`)**:
   - `Curso`: atributos `id_curso`, `nome_curso`, `horas_exigidas`, `coordenador`, getters/setters e `to_string()`.
   - `Controller_Curso`:
     - `inserir_curso()`: verifica se `id_curso` já existe (`find_one`), solicita os dados, executa `insert_one` e exibe o objeto criado.
     - `atualizar_curso()`: lista os cursos em `DataFrame`, solicita `id_curso`, executa `update_one({"id_curso": id_curso}, {"$set": ...})` e exibe o registro atualizado (item 7.d.7).
     - `excluir_curso()`: lista os cursos e chama `excluir_registro_seguro("cursos", id_curso, ...)` para validar se há alunos vinculados antes de excluir.

---

### 👤 Membro 2 (Issacar): Model e CRUD de `alunos`

1. **Model de Aluno (`src/model/aluno.py`)**:
   - Atributos: `matricula`, `nome_aluno`, `email`, `periodo` e **`curso: Curso`** (exigência da Etapa 2 do edital: armazenar a instância do objeto `Curso` associado, não apenas o `id_curso`).
   - Getters, setters e método `to_string()` exibindo também o nome do curso.
2. **Controller de Aluno (`src/controller/controller_aluno.py`)**:
   - `inserir_aluno()`: verifica se a `matricula` já existe, lista os cursos disponíveis na coleção `cursos`, valida se o `id_curso` informado existe, insere com `insert_one` e retorna o objeto `Aluno` montado.
   - `atualizar_aluno()`: lista os alunos (com lookup/nome do curso), permite alterar `nome_aluno`, `email`, `periodo` e `id_curso` via `update_one({"matricula": matricula}, {"$set": ...})` e exibe o aluno atualizado.
   - `excluir_aluno()`: lista os alunos e utiliza `excluir_registro_seguro("alunos", matricula, ...)` para verificar se o aluno possui tickets em `tickets_atividades`.

---

### 👤 Membro 3 (Bruno): Model e CRUD de `categorias_atividade` & Exclusão Segura (`exclusao_segura.py`)

1. **Model de Categoria de Atividade (`src/model/categoria_atividade.py`)**:
   - Atributos: `id_categoria`, `nome_categoria`, `limite_maximo_horas`, `descricao`.
   - Getters, setters e método `to_string()`.
2. **Controller de Categoria (`src/controller/controller_categoria_atividade.py`)**:
   - `inserir_categoria()`, `atualizar_categoria()`, `excluir_categoria()` e `verifica_existencia()` operando na coleção `categorias_atividade`.
3. **Padrão de Exclusão Segura no MongoDB (`src/utils/exclusao_segura.py`)**:
   - Implementar a regra do **item 7.c.5.i do edital** para o MongoDB:
     1. Confirmar com o usuário se deseja realmente remover o documento;
     2. Verificar no mapa `DEPENDENCIAS` (usando `count_documents`) se o documento possui referências em coleções filhas (`cursos` → `alunos` → `tickets_atividades`; `categorias_atividade` → `tickets_atividades`; `administradores` → `tickets_atividades`);
     3. Caso possua dependentes, informar a quantidade encontrada em cada coleção filha e perguntar se o usuário deseja remover também os documentos das coleções filhas (exclusão em cascata recursiva com `delete_many` / `delete_one`) ou cancelar.

---

### 👤 Membro 4 (Daniel): Model e CRUD de `administradores` & Relatórios (`relatorios.py`)

1. **Model e Controller de Administrador (`src/model/administrador.py` e `src/controller/controller_administrador.py`)**:
   - `Administrador`: atributos `id_admin`, `nome_admin`, `email`, `cargo`, getters/setters e `to_string()`.
   - `Controller_Administrador`: métodos `inserir_administrador()`, `atualizar_administrador()`, `excluir_administrador()` (com trava de FK em `tickets_atividades.id_admin_avaliador`) e `verifica_existencia()`.
2. **Módulo de Relatórios com Aggregation Pipeline (`src/reports/relatorios.py`)**:
   - **Relatórios de Sumarização / Agrupamento (`$group` — Item 7.a.1.i — vale 1,0 ponto):**
     1. `get_relatorio_horas_por_aluno()`: agrupa `tickets_atividades` por `matricula_aluno` (somando `horas_solicitadas`, `horas_validadas` dos aprovados e quantidade de tickets) com `$lookup` em `alunos` e `cursos` para comparar o total validado com as `horas_exigidas` do curso.
     2. `get_relatorio_tickets_por_categoria()`: agrupa `tickets_atividades` por `id_categoria` (`$group` com `$sum` de horas solicitadas, horas validadas e contagem de tickets) com `$lookup` em `categorias_atividade`.
     3. `get_relatorio_tickets_por_status()`: agrupa `tickets_atividades` por `status` (`APROVADO`, `PENDENTE`, `RECUSADO`) contando total de tickets e soma de horas.
   - **Relatórios com Junção de Coleções (`$lookup` — Item 7.a.1.ii — vale 0,5 ponto):**
     4. `get_relatorio_tickets_detalhado()`: pipeline com `$lookup` juntando `tickets_atividades` + `alunos` + `cursos` + `categorias_atividade` + `administradores` (com `preserveNullAndEmptyArrays: True` para tickets ainda pendentes sem avaliador).
     5. `get_relatorio_alunos_e_cursos()`: `$lookup` juntando `alunos` e `cursos`.
   - **Relatórios de Listagem das Coleções:**
     6. Listagens ordenadas de `cursos`, `categorias_atividade` e `administradores`.

---

### 👤 Membro 5 (Werney): Menus, Splash Screen, Docker, Diagramas, README e Vídeo

1. **Splash Screen e Configurações (`src/utils/splash_screen.py` e `src/utils/config.py`)**:
   - `query_count(collection_name)` executando `mongo.db[collection_name].count_documents({})` para as 5 coleções (item 6.d).
   - Exibição dos 6 integrantes do grupo, professor, disciplina e semestre `2026/2` (item 6.c).
2. **Menu Principal (`src/principal.py`)**:
   - Fluxo constante de menu e submenus (itens 6.f e 6.g).
   - Loop `"Deseja inserir/atualizar/excluir mais algum registro? (S/N)"` após cada operação (itens 7.b.5, 7.c.6, 7.d.8).
   - Atualização da Splash Screen ao retornar ao menu principal.
3. **Infraestrutura e Documentação (`docker-compose.yml`, `diagramas/`, `README.md`)**:
   - Container Docker do MongoDB (`mongo:7` na porta `27017`).
   - Diagrama Relacional e ER em Mermaid (`diagramas/diagrama_logico.mmd` e `diagramas/diagrama_ER.mmd`) e exportação em PNG/PDF.
   - `README.md` detalhando a execução no Linux / VM LabDatabase e link para o vídeo demonstrativo no YouTube.

---

### 👤 Membro 6 (Gabriel): Model e CRUD de `tickets_atividades` & Regras de Horas Complementares

1. **Model de Ticket de Atividade (`src/model/ticket_atividade.py`)**:
   - Atributos: `id_ticket`, `titulo`, `horas_solicitadas`, `horas_validadas`, `status`, `observacao_admin`, além das instâncias associadas **`aluno: Aluno`**, **`categoria: CategoriaAtividade`** e **`admin_avaliador: Administrador | None`** (conforme Etapa 2 do edital).
   - Getters, setters e método `to_string()`.
2. **Controller de Ticket de Atividade (`src/controller/controller_ticket_atividade.py`)**:
   - `inserir_ticket()`:
     - Verifica se `id_ticket` já existe;
     - Lista alunos (`alunos`) e valida `matricula_aluno`;
     - Lista categorias (`categorias_atividade`) e valida `id_categoria`;
     - Valida a regra de negócio herdada do projeto de Horas Complementares: `horas_solicitadas > 0` e verifica se as horas respeitam o `limite_maximo_horas` da categoria;
     - Permite informar status (`PENDENTE`, `APROVADO`, `RECUSADO`), `id_admin_avaliador` (opcional se `PENDENTE`), `horas_validadas` e `observacao_admin`;
     - Insere com `insert_one` e exibe o `to_string()` do novo ticket.
   - `atualizar_ticket()`:
     - Lista os tickets cadastrados, seleciona por `id_ticket`, permite atualizar título, categoria, horas solicitadas, avaliação do administrador (`status`, `horas_validadas`, `id_admin_avaliador`, `observacao_admin`), executa `update_one` e exibe o documento atualizado.
   - `excluir_ticket()`:
     - Lista os tickets e remove usando `excluir_registro_seguro("tickets_atividades", id_ticket, ...)`.
