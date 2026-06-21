class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEspera:
    def __init__(self):
        self.head = None
        self.contadorV = 1
        self.contadorA = 201

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == "A":
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do paciente (A/V): ").upper()

        if cor == "V":
            numero = self.contadorV
            self.contadorV += 1
        elif cor == "A":
            numero = self.contadorA
            self.contadorA += 1
        else:
            print("Cor inválida!")
            return

        novo = Nodo(numero, cor)

        if self.head is None:
            self.head = novo
        elif cor == "V":
            self.inserirSemPrioridade(novo)
        else:
            self.inserirComPrioridade(novo)

    def imprimirListaEspera(self):
        atual = self.head

        if atual is None:
            print("Fila vazia!")
            return

        while atual:
            print(f"{atual.cor}{atual.numero}", end=" -> ")
            atual = atual.proximo

        print("None")

    def atenderPaciente(self):
        if self.head is None:
            print("Fila vazia!")
        else:
            print(f"Chamando paciente: {self.head.cor}{self.head.numero}")
            self.head = self.head.proximo


# ===== MENU =====
lista = ListaEspera()

while True:
    print("\n1 - Adicionar paciente")
    print("2 - Mostrar fila")
    print("3 - Atender paciente")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        lista.inserir()
    elif op == "2":
        lista.imprimirListaEspera()
    elif op == "3":
        lista.atenderPaciente()
    elif op == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")