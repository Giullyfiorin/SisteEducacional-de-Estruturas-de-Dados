class Nodo:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None


class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def funcaoHash(self, sigla):
        if sigla == "DF":
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, sigla, nome):
        pos = self.funcaoHash(sigla)
        novo = Nodo(sigla, nome)

        novo.proximo = self.tabela[pos]
        self.tabela[pos] = novo

    def imprimir(self):
        for i in range(10):
            atual = self.tabela[i]
            print(f"{i}:", end=" ")

            while atual is not None:
                print(atual.sigla, end=" -> ")
                atual = atual.proximo

            print("None")


tabela = TabelaHash()

print("Tabela vazia:")
tabela.imprimir()

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

print("\nTabela com estados:")
tabela.imprimir()

tabela.inserir("GF", "Giully Fiorin")

print("\nTabela com estado fictício:")
tabela.imprimir()
