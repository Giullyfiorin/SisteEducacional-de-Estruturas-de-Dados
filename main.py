from estruturas.fila_hospital import menu_fila_hospitalar
from estruturas.tabela_hash import menu_tabela_hash


def mostrar_sobre_projeto():
    print("\n=== SOBRE O PROJETO ===")
    print("Sistema Educacional de Estruturas de Dados em Python.")
    print()
    print("Estruturas implementadas:")
    print("- Lista Encadeada")
    print("- Fila Hospitalar com Prioridade")
    print("- Tabela Hash com Encadeamento")
    print()
    print("Desenvolvido por Giully Fiorin")


def menu_principal():
    """Menu principal do sistema."""
    while True:
        print("\n======================================")
        print(" SISTEMA EDUCACIONAL DE ESTRUTURAS")
        print("======================================")
        print("1 - Fila Hospitalar com Prioridade")
        print("2 - Tabela Hash de Estados")
        print("3 - Sobre o Projeto")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_fila_hospitalar()

        elif opcao == "2":
            menu_tabela_hash()

        elif opcao == "3":
            mostrar_sobre_projeto()

        elif opcao == "4":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()