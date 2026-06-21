class NodoHash:
    """
    Representa um item dentro da tabela hash.
    Cada nodo armazena a sigla, o nome do estado e a referência para o próximo item.
    """

    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None


class TabelaHash:
    """
    Tabela Hash com encadeamento para tratamento de colisões.
    """

    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def funcao_hash(self, sigla):
        """
        Calcula a posição da sigla na tabela.
        O DF recebe uma posição fixa por regra especial do exercício.
        """
        sigla = sigla.upper()

        if sigla == "DF":
            return 7

        return (ord(sigla[0]) + ord(sigla[1])) % self.tamanho

    def inserir(self, sigla, nome):
        """Insere uma nova sigla na tabela hash."""
        sigla = sigla.upper()
        posicao = self.funcao_hash(sigla)

        if self.buscar(sigla):
            print(f"A sigla {sigla} já está cadastrada.")
            return

        novo = NodoHash(sigla, nome)

        novo.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo

        print(f"{sigla} - {nome} inserido na posição {posicao}.")

    def buscar(self, sigla):
        """Busca um estado pela sigla."""
        sigla = sigla.upper()
        posicao = self.funcao_hash(sigla)
        atual = self.tabela[posicao]

        while atual is not None:
            if atual.sigla == sigla:
                return atual

            atual = atual.proximo

        return None

    def remover(self, sigla):
        """Remove um estado da tabela hash pela sigla."""
        sigla = sigla.upper()
        posicao = self.funcao_hash(sigla)
        atual = self.tabela[posicao]
        anterior = None

        while atual is not None:
            if atual.sigla == sigla:
                if anterior is None:
                    self.tabela[posicao] = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                print(f"{sigla} removido da tabela.")
                return

            anterior = atual
            atual = atual.proximo

        print(f"Sigla {sigla} não encontrada.")

    def imprimir(self):
        """Exibe a tabela hash completa."""
        print("\n=== TABELA HASH ===")

        for i in range(self.tamanho):
            atual = self.tabela[i]
            print(f"{i}:", end=" ")

            while atual is not None:
                print(f"{atual.sigla}", end=" -> ")
                atual = atual.proximo

            print("None")

    def estatisticas(self):
        """Mostra informações gerais sobre a tabela hash."""
        total_itens = 0
        posicoes_ocupadas = 0
        colisoes = 0

        for posicao in self.tabela:
            atual = posicao
            quantidade_na_posicao = 0

            while atual is not None:
                total_itens += 1
                quantidade_na_posicao += 1
                atual = atual.proximo

            if quantidade_na_posicao > 0:
                posicoes_ocupadas += 1

            if quantidade_na_posicao > 1:
                colisoes += quantidade_na_posicao - 1

        print("\n=== ESTATÍSTICAS ===")
        print(f"Total de itens cadastrados: {total_itens}")
        print(f"Posições ocupadas: {posicoes_ocupadas}")
        print(f"Colisões identificadas: {colisoes}")


def carregar_estados(tabela):
    """Carrega os estados brasileiros na tabela hash."""
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"),
        ("AM", "Amazonas"), ("BA", "Bahia"), ("CE", "Ceará"),
        ("ES", "Espírito Santo"), ("GO", "Goiás"), ("MA", "Maranhão"),
        ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"),
        ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"),
        ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins"),
        ("DF", "Distrito Federal")
    ]

    for sigla, nome in estados:
        tabela.inserir(sigla, nome)


def menu_tabela_hash():
    """Menu interativo da tabela hash."""
    tabela = TabelaHash()
    estados_carregados = False

    while True:
        print("\n=== TABELA HASH DE ESTADOS ===")
        print("1 - Carregar estados brasileiros")
        print("2 - Inserir novo item")
        print("3 - Buscar por sigla")
        print("4 - Remover por sigla")
        print("5 - Mostrar tabela")
        print("6 - Mostrar estatísticas")
        print("7 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if estados_carregados:
                print("Os estados brasileiros já foram carregados.")
            else:
                carregar_estados(tabela)
                estados_carregados = True

        elif opcao == "2":
            sigla = input("Digite a sigla: ")
            nome = input("Digite o nome: ")
            tabela.inserir(sigla, nome)

        elif opcao == "3":
            sigla = input("Digite a sigla para buscar: ")
            resultado = tabela.buscar(sigla)

            if resultado:
                print(f"Encontrado: {resultado.sigla} - {resultado.nome}")
            else:
                print("Sigla não encontrada.")

        elif opcao == "4":
            sigla = input("Digite a sigla para remover: ")
            tabela.remover(sigla)

        elif opcao == "5":
            tabela.imprimir()

        elif opcao == "6":
            tabela.estatisticas()

        elif opcao == "7":
            break

        else:
            print("Opção inválida. Tente novamente.")