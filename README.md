# 4HC1-Banco-de-Dados_Trabalho-C3_CONTROLE-HORAS-COMPLEMENTARES

Sistema de gerenciamento e validação de **Horas Complementares Acadêmicas** via terminal (CLI) integrado ao banco de dados não relacional **MongoDB** via Docker / VM LabDatabase, utilizando `pymongo` e `pandas` (sem ODM/ORM).

---

## 🎥 Vídeo de Demonstração (YouTube)

- **Link do vídeo:** *(Inserir link do YouTube aqui antes da entrega final)*

---

## 👥 Integrantes do Grupo (4HC1 - 2026/2)

- Bruno Mauro Bayer Laiber
- Daniel Lima Del'Antonio
- Gabriel Antônio Galdino dos Santos
- Issacar Mattos Gutler
- Kaike Vaccari do Nascimento
- Werney Ferreira Rocha

**Professor:** Prof. M.Sc. Howard Roatti  
**Disciplina:** Banco de Dados — FAESA  

---

## 🗄️ Coleções do Sistema no MongoDB (`labdatabase`)

1. **`cursos`**: Cadastro de cursos de graduação e total de horas complementares exigidas (`id_curso`, `nome_curso`, `horas_exigidas`, `coordenador`).
2. **`alunos`**: Cadastro de estudantes vinculados a um curso (`matricula`, `nome_aluno`, `email`, `periodo`, `id_curso`).
3. **`categorias_atividade`**: Categorias de atividades complementares e seus limites máximos de aproveitamento (`id_categoria`, `nome_categoria` [`CURSO`, `EVENTO`, `PESQUISA`], `limite_maximo_horas`, `descricao`).
4. **`administradores`**: Coordenadores e avaliadores responsáveis por validar os certificados (`id_admin`, `nome_admin`, `email`, `cargo`).
5. **`tickets_atividades`**: Solicitações (tickets) de horas complementares enviadas pelos alunos e avaliadas pelos administradores (`id_ticket`, `matricula_aluno`, `id_categoria`, `id_admin_avaliador`, `titulo`, `horas_solicitadas`, `horas_validadas`, `status`, `observacao_admin`).

---

## 🚀 Passo a Passo para Executar o Projeto (Linux / VM LabDatabase)

### 1. Preparar o Ambiente e Instalar Dependências

**No Linux / VM LabDatabase:**
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

**No Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

---

### 2. Iniciar o Banco de Dados (MongoDB via Docker)

Caso esteja na **VM LabDatabase** e o container `mongo` já exista:
```bash
docker start mongo
docker ps
```

Ou suba o container do MongoDB diretamente pelo `docker-compose.yml` deste repositório:
```bash
sudo docker compose up -d
sudo docker compose ps
```
*(No Windows com Docker Desktop, não é necessário usar `sudo`: `docker compose up -d`)*

O serviço `mongo` responderá na porta padrão **`27017`**.

---

### 3. Criar as Coleções e Carga Inicial de Documentos

Antes de abrir o sistema pela primeira vez (ou para resetar os dados de exemplo), execute o script de criação das coleções (Item 5 do Edital):

**No Linux / macOS:**
```bash
python3 src/createCollectionsAndData.py
```

**No Windows:**
```powershell
python src/createCollectionsAndData.py
```

---

### 4. Executar a Aplicação Principal no Terminal

A partir da raiz do projeto, execute:

**No Linux / macOS:**
```bash
python3 src/principal.py
```

**No Windows:**
```powershell
python src/principal.py
```

---

## ⚙️ Configuração de Conexão com o MongoDB

Por padrão, o módulo `src/conexion/mongo_queries.py` conecta em `localhost:27017` no database `labdatabase`.
- Se o arquivo `src/conexion/passphrase/authentication.mongo` contiver usuário e senha (formato `usuario,senha`), a conexão autenticada é utilizada automaticamente (e se o MongoDB local/VM estiver rodando sem autenticação obrigatória, o módulo faz fallback automático para conexão direta).
- Também é possível sobrescrever via variáveis de ambiente: `MONGO_HOST`, `MONGO_PORT`, `MONGO_DB`, `MONGO_USER` e `MONGO_PASSWORD`.

---

### Encerrar o Container do Banco de Dados

Quando terminar de utilizar a aplicação:
```bash
docker compose down
```
