from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_curso import Controller_Curso
from controller.controller_aluno import Controller_Aluno
from controller.controller_categoria_atividade import Controller_Categoria_Atividade
from controller.controller_administrador import Controller_Administrador
from controller.controller_ticket_atividade import Controller_Ticket_Atividade

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_curso = Controller_Curso()
ctrl_aluno = Controller_Aluno()
ctrl_categoria = Controller_Categoria_Atividade()
ctrl_administrador = Controller_Administrador()
ctrl_ticket = Controller_Ticket_Atividade()


def reports(opcao_relatorio: int = 0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_horas_por_aluno()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_tickets_por_categoria()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_tickets_por_status()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_tickets_detalhado()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_alunos_e_cursos()
    elif opcao_relatorio == 6:
        relatorio.get_relatorio_cursos()
    elif opcao_relatorio == 7:
        relatorio.get_relatorio_categorias()
    elif opcao_relatorio == 8:
        relatorio.get_relatorio_administradores()


def inserir(opcao_inserir: int = 0):
    if opcao_inserir == 1:
        ctrl_curso.inserir_curso()
    elif opcao_inserir == 2:
        ctrl_aluno.inserir_aluno()
    elif opcao_inserir == 3:
        ctrl_categoria.inserir_categoria()
    elif opcao_inserir == 4:
        ctrl_administrador.inserir_administrador()
    elif opcao_inserir == 5:
        ctrl_ticket.inserir_ticket()


def atualizar(opcao_atualizar: int = 0):
    if opcao_atualizar == 1:
        ctrl_curso.atualizar_curso()
    elif opcao_atualizar == 2:
        ctrl_aluno.atualizar_aluno()
    elif opcao_atualizar == 3:
        ctrl_categoria.atualizar_categoria()
    elif opcao_atualizar == 4:
        ctrl_administrador.atualizar_administrador()
    elif opcao_atualizar == 5:
        ctrl_ticket.atualizar_ticket()


def remover(opcao_excluir: int = 0):
    if opcao_excluir == 1:
        ctrl_curso.excluir_curso()
    elif opcao_excluir == 2:
        ctrl_aluno.excluir_aluno()
    elif opcao_excluir == 3:
        ctrl_categoria.excluir_categoria()
    elif opcao_excluir == 4:
        ctrl_administrador.excluir_administrador()
    elif opcao_excluir == 5:
        ctrl_ticket.excluir_ticket()


def _continuar(acao: str) -> bool:
    resposta = input(f"\nDeseja {acao} mais algum documento? (S/N): ").strip().upper()
    return resposta in {"S", "SIM"}


def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = input("Escolha uma opção [1-5]: ").strip()
        config.clear_console(1)

        if opcao == "1":  # Relatórios
            while True:
                print(config.MENU_RELATORIOS)
                try:
                    opcao_relatorio = int(input("Escolha uma opção [0-8]: ").strip())
                except ValueError:
                    print("Opção inválida.")
                    config.clear_console(1)
                    continue
                config.clear_console(1)

                if opcao_relatorio == 0:
                    break

                reports(opcao_relatorio)
                config.clear_console(1)

        elif opcao == "2":  # Inserir Documentos
            while True:
                print(config.MENU_ENTIDADES)
                try:
                    opcao_inserir = int(input("Escolha uma opção [1-5]: ").strip())
                except ValueError:
                    print("Opção inválida.")
                    config.clear_console(1)
                    break
                config.clear_console(1)

                inserir(opcao_inserir=opcao_inserir)
                config.clear_console(1)

                if not _continuar("inserir"):
                    break

            print(tela_inicial.get_updated_screen())
            config.clear_console(1)

        elif opcao == "3":  # Atualizar Documentos
            while True:
                print(config.MENU_ENTIDADES)
                try:
                    opcao_atualizar = int(input("Escolha uma opção [1-5]: ").strip())
                except ValueError:
                    print("Opção inválida.")
                    config.clear_console(1)
                    break
                config.clear_console(1)

                atualizar(opcao_atualizar=opcao_atualizar)
                config.clear_console(1)

                if not _continuar("atualizar"):
                    break

            print(tela_inicial.get_updated_screen())
            config.clear_console(1)

        elif opcao == "4":  # Remover Documentos
            while True:
                print(config.MENU_ENTIDADES)
                try:
                    opcao_excluir = int(input("Escolha uma opção [1-5]: ").strip())
                except ValueError:
                    print("Opção inválida.")
                    config.clear_console(1)
                    break
                config.clear_console(1)

                remover(opcao_excluir=opcao_excluir)
                config.clear_console(1)

                if not _continuar("excluir"):
                    break

            print(tela_inicial.get_updated_screen())
            config.clear_console(1)

        elif opcao == "5":  # Sair
            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o Sistema de Controle de Horas Complementares!")
            exit(0)

        else:
            print("Opção inválida.")
            config.clear_console(1)


if __name__ == "__main__":
    run()
