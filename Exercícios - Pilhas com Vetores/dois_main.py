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
    
    def esvaziar_pilha(self):
        while self.n > 0:
            print("numero desempilhado:", self.pilha_pop())
        print("Pilha esvaziada")




# Criar pilha com capacidade 10
pilha = Pilha(10)

# Empilhar de 1 a 5
for i in range(1, 6):
    pilha.pilha_push(i)

# Desempilhar todos os elementos
print("\nDesempilhando todos os elementos:")
# for _ in range(5):
#     print(pilha.pilha_pop())

pilha.esvaziar_pilha()

print("\nPilha após desempilhar todos os elementos:", pilha.vetor)
