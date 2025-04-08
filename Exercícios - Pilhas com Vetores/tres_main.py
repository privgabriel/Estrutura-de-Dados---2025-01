class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.n = 0
        self.vetor = []

    def pilha_push(self, valor):
        if self.n == self.capacidade:
            print("Pilha cheia")
            return
        self.vetor.append(valor)
        self.n += 1
        print("Empilhando:", valor)

    def pilha_pop(self):
        if self.n == 0:
            print("Pilha vazia")
            return None
        self.n -= 1
        return self.vetor.pop()

    def pilha_topo(self):
        if self.n == 0:
            print("Pilha vazia")
            return None
        return self.vetor[self.n - 1]


# Criar pilha com capacidade 5
pilha = Pilha(5)

# Solicitar 5 números ao usuário
for i in range(5):
    valor = int(input(f"Digite o {i + 1}º número: "))
    pilha.pilha_push(valor)

# Desempilhar e mostrar os valores na ordem inversa
print("\nDesempilhando os valores (ordem inversa):")
while pilha.n > 0:
    print(pilha.pilha_pop())

print("\nPilha após esvaziar:", pilha.vetor)
