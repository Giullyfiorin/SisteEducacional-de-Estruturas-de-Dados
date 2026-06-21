class Nodo:
    """
    Representa um paciente dentro da fila.
    Cada paciente possui uma cor, um número e uma referência para o próximo paciente.
    """

    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEspera:
    """
    Lista encadeada usada para simular uma fila hospitalar com prioridade.

    Pacientes com cor A possuem prioridade.
    Pacientes com cor V são atendidos por ordem de chegada.
    """

    def __init__(self):
        self.head = None
        self.contador_verde = 1
        self.contador_amarelo = 201

    def inserir_sem_prioridade(self, nodo):
        """Insere pacientes sem prioridade no final da fila."""
        if self.head is None:
            self.head = nodo
            return

        atual = self.head

        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = nodo

    def inserir_com_prioridade(self, nodo):
        """
        Insere pacientes com prioridade antes dos pacientes sem prioridade,
        mantendo a ordem de chegada entre os prioritários.
        """
        if self.head is None or self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
            return

        atual = self.head

        while atual.proximo is not None and atual.proximo.cor == "A":
            atual = atual.proximo

        nodo.proximo = atual.proximo
        atual.proximo = nodo

    def adicionar_paciente(self, cor):
        """Adiciona um novo paciente na fila conforme sua classificação."""
        cor = cor.upper()

        if cor == "V":
            numero = self.contador_verde
            self.contador_verde += 1
            novo = Nodo(numero, cor)
            self.inserir_sem_prioridade(novo)

        elif cor == "A":
            numero = self.contador_amarelo
            self.contador_amarelo += 1
            novo = Nodo(numero, cor)
            self.inserir_com_prioridade(novo)

        else:
            print("Classificação inválida. Use A para prioridade ou V para comum.")
            return

        print(f"Paciente {cor}{numero} adicionado à fila.")

    def mostrar_fila(self):
        """Exibe todos os pacientes aguardando atendimento."""
        if self.head is None:
            print("Fila vazia.")
            return

        atual = self.head
        print("\nFila de espera:")

        while atual is not None:
            print(f"{atual.cor}{atual.numero}", end=" -> ")
            atual = atual.proximo

        print("None")

    def atender_paciente(self):
        """Remove o primeiro paciente da fila e simula o atendimento."""
        if self.head is None:
            print("Não há pacientes para atender.")
            return

        paciente = self.head
        self.head = self.head.proximo

        print(f"Chamando paciente: {paciente.cor}{paciente.numero}")

    def contar_pacientes(self):
        """Conta quantos pacientes ainda estão aguardando na fila."""
        total = 0
        atual = self.head

        while atual is not None:
            total += 1
            atual = atual.proximo

        return total


def menu_fila_hospitalar():
    """Menu interativo da fila hospitalar."""
    fila = ListaEspera()

    while True:
        print("\n=== FILA HOSPITALAR COM PRIORIDADE ===")
        print("1 - Adicionar paciente")
        print("2 - Mostrar fila")
        print("3 - Atender paciente")
        print("4 - Mostrar total de pacientes")
        print("5 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cor = input("Digite a classificação do paciente (A/V): ")
            fila.adicionar_paciente(cor)

        elif opcao == "2":
            fila.mostrar_fila()

        elif opcao == "3":
            fila.atender_paciente()

        elif opcao == "4":
            total = fila.contar_pacientes()
            print(f"Total de pacientes aguardando: {total}")

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")