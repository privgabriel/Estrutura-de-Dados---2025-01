class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.vetor = []
        self.n = 0

    def pilha_push(self, valor):
        if self.n >= self.capacidade:
            print("Pilha cheia")
            return
        self.vetor.append(valor)
        self.n += 1

    def pilha_pop(self):
        if self.n == 0:
            return None
        self.n -= 1
        return self.vetor.pop()

    def pilha_topo(self):
        if self.n == 0:
            return None
        return self.vetor[-1]

    def mostrar_pilha(self):
        return self.vetor.copy()

    def remover_item(self, item_remover):
        pilha_auxiliar = []
        encontrado = False

        # Desempilha até encontrar o item
        while self.n > 0:
            topo = self.pilha_pop()
            if topo == item_remover and not encontrado:
                encontrado = True
                continue  # não empilha o item a ser removido
            pilha_auxiliar.append(topo)

        # Reempilha os itens de volta (na ordem correta)
        while pilha_auxiliar:
            self.pilha_push(pilha_auxiliar.pop())

        if encontrado:
            print(f"Item '{item_remover}' removido da pilha.")
        else:
            print(f"Item '{item_remover}' não encontrado na pilha.")

# Criando a pilha
pilha = Pilha(10)

# Empilhando valores
for valor in [10, 20, 30, 40, 50]:
    pilha.pilha_push(valor)

print("Pilha original:", pilha.mostrar_pilha())

# Remover item do meio (por exemplo, 30)
pilha.remover_item(30)

print("Pilha após remover 30:", pilha.mostrar_pilha())

