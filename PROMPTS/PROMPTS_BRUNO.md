# Registro de Uso de IA — Membro 3 (Bruno Mauro Bayer Laiber)

Este arquivo registra o uso de IA no desenvolvimento da coleção `categorias_atividade` e do módulo de exclusão segura no MongoDB, conforme a Observação (5) do edital da C3.

## Prompt 1

- **Data** — 27/11/2026
- **Fonte** — ChatGPT (Codex)
- **Prompt utilizado**

  > [Edital C3](https://github.com/Werney-FAESA/4HC1-Banco-de-Dados_Trabalho-C3_CONTROLE-HORAS-COMPLEMENTARES/blob/main/C3_Edital_Desenvolvimento_Banco_N%C3%A3o_Relacional_-_Valor_8_Pontos_-_Grupo/C3_Edital_Desenvolvimento_Banco_N%C3%A3o_Relacional_-_Valor_8_Pontos_-_Grupo.md)
  >
  > sou o membro 3 e faça o que deve ser feito do membro 3 e crie um branch e poste nela. Pode ter acesso total ao meu computador pra fazer.

- **Uso da resposta** — O Codex conferiu o edital e os arquivos `LISTA_MEMBROS_E_TAREFAS.md` e `PASSO_1.md` para identificar a entrega e o nome da branch do membro 3.

## Prompt 2

- **Data** — 27/11/2026
- **Fonte** — ChatGPT (Codex)
- **Prompt utilizado**

  > [Edital C3](https://github.com/Werney-FAESA/4HC1-Banco-de-Dados_Trabalho-C3_CONTROLE-HORAS-COMPLEMENTARES/blob/main/C3_Edital_Desenvolvimento_Banco_N%C3%A3o_Relacional_-_Valor_8_Pontos_-_Grupo/C3_Edital_Desenvolvimento_Banco_N%C3%A3o_Relacional_-_Valor_8_Pontos_-_Grupo.md)
  >
  > sou o membro Bruno Mauro Bayer Laiber e faça o que deve ser feito do membro Bruno e crie um branch e poste nela. Pode ter acesso total ao meu computador pra fazer.

- **Uso da resposta** — O Codex revisou o modelo `CategoriaAtividade`, implementou seu CRUD e adicionou a exclusão segura compartilhada. A confirmação mostra o número de registros afetados em cada coleção. Se o usuário autorizar a cascata, os tickets são removidos antes dos alunos quando o registro principal é um curso.
- **Verificação** — Os sete testes existentes passaram. A integração foi executada em um MongoDB 7.0 com os dados iniciais do projeto. Foram verificados cadastro, ID duplicado, listagem, atualização parcial, exclusão sem dependentes, recusa da cascata, alteração dos vínculos durante a confirmação e exclusão de curso com alunos e tickets.
