Registro de Uso de IA — Membro 2 (Issacar Mattos Gutler)

Este arquivo registra o uso de IA como apoio ao desenvolvimento de
src/model/aluno.py e src/controller/controller_aluno.py, conforme a Observação
(5) do edital da C3.

Prompt #1 — Contextualização do projeto e definição das tarefas

Data: 27/11/2026

Fonte: ChatGPT

Prompt utilizado:

Segue o arquivo com a estrutura do projeto C3. Minha responsabilidade como Membro 2 é desenvolver a modelagem e o CRUD completo da entidade Aluno (src/model/aluno.py e src/controller/controller_aluno.py), integrando com MongoDB e respeitando as regras do edital. Vamos estruturar o desenvolvimento passo a passo a partir disso.

O que foi feito com a resposta: o contexto do repositório e o escopo do Membro 2 foram compreendidos e divididos em etapas sequenciais de implementação (modelagem, cadastro, listagem, atualização, exclusão e testes), servindo de base para os prompts seguintes.

Prompt #2 — Modelagem do aluno

Data: 27/11/2026

Fonte: Codex

Prompt utilizado:

Analise a classe Aluno existente e compare com os requisitos do edital. Verifique os atributos, getters, setters e a associação com a classe Curso. Sugira apenas os ajustes necessários, mantendo o padrão do projeto.

O que foi feito com a resposta: validou-se que a classe Aluno já contemplava os atributos matricula, nome_aluno, email, periodo e uma instância de Curso, além dos métodos getters, setters e to_string() exibindo o nome do curso associado. Foi removido apenas um comentário TODO desatualizado.

Prompt #3 — Cadastro e validações

Data: 27/11/2026

Fonte: Codex

Prompt utilizado:

Implemente o cadastro de alunos no MongoDB com pymongo, verificando matrícula duplicada, existência do curso e validade dos campos. Mantenha compatibilidade com a camada MongoQueries existente e explique como testar.

O que foi feito com a resposta: implementada a verificação de duplicidade de matrícula via find_one({"matricula": matricula}), a listagem de cursos disponíveis e a confirmação da existência de id_curso antes da inserção com insert_one. O documento persistido em alunos armazena apenas id_curso, enquanto o objeto retornado em memória recebe a instância completa de Curso.

Prompt #4 — Listagem e relacionamento

Data: 27/11/2026

Fonte: Codex

Prompt utilizado:

Crie a listagem dos alunos com Aggregation Pipeline e $lookup entre alunos e cursos. Exiba matrícula, nome, e-mail, período e nome do curso em formato legível no terminal.

O que foi feito com a resposta: construída a pipeline de agregação unindo as coleções alunos e cursos por meio de $lookup (localField: "id_curso", foreignField: "id_curso"), seguida de $unwind e $project para formatar e exibir matrícula, nome, e-mail, período, ID e nome do curso no terminal.

Prompt #5 — Atualização

Data: 27/11/2026

Fonte: Codex

Prompt utilizado:

Implemente a atualização de alunos com update_one e $set. Permita manter os valores existentes pressionando Enter, valide mudanças de curso e apresente o documento atualizado.

O que foi feito com a resposta: desenvolvida a rotina de edição mantendo matricula como identificador imutável. A interface exibe os alunos cadastrados, permite pressionar Enter para preservar valores atuais, revalida o curso caso alterado e aplica as mudanças no banco via update_one({"matricula": matricula}, {"$set": novos_dados}).

Prompt #6 — Exclusão e integração

Data: 27/11/2026

Fonte: Codex

Prompt utilizado:

Integre excluir_aluno() ao módulo de exclusão segura do grupo, garantindo confirmação e tratamento de tickets vinculados. Identifique dependências ainda não implementadas sem modificar arquivos de outros integrantes.

O que foi feito com a resposta: implementada a listagem e verificação de existência da matrícula na controladora antes de delegar a remoção para excluir_registro_seguro("alunos", matricula, f"o aluno '{nome_aluno}'"). A confirmação do usuário e o bloqueio por tickets vinculados ficaram centralizados no módulo compartilhado exclusao_segura.py (responsabilidade do membro 3), sem alterações em arquivos de terceiros.

Prompt #7 — Testes e revisão

Data: 27/11/2026

Fonte: Codex

Prompt utilizado:

Revise o CRUD de alunos com base no edital da C3. Teste cadastros válidos e inválidos, matrícula duplicada, curso inexistente, atualização, listagem e exclusão. Informe o que foi efetivamente testado e quais pendências ainda existem.

O que foi feito com a resposta: criados e executados testes cobrindo a associação Aluno–Curso, a consulta com $lookup, o bloqueio de matrícula duplicada e curso inexistente, o cadastro válido, a atualização com update_one e a chamada à exclusão segura. Os testes unitários/isolados passaram, restando como pendência apenas o teste integrado da exclusão real após a conclusão do módulo do membro 3.