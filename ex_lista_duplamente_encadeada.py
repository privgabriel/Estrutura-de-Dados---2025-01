import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def inserir_final(self, data):
        novo = Node(data)
        if not self.head:
            self.head = novo
            novo.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = novo
            novo.next = self.head

    def buscar(self, valor):
        if not self.head:
            return False
        temp = self.head
        while True:
            if temp.data == valor:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def remover(self, valor):
        if not self.head:
            return
        atual = self.head
        anterior = None
        while True:
            if atual.data == valor:
                if anterior:
                    anterior.next = atual.next
                else:
                    if atual.next == self.head:
                        self.head = None
                        return
                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = atual.next
                        self.head = atual.next
                return
            anterior = atual
            atual = atual.next
            if atual == self.head:
                break

    def contar_elementos(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

    def __str__(self):
        if not self.head:
            return "[]"
        result = []
        temp = self.head
        while True:
            result.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        return " -> ".join(result) + " (circular)"

# Desafio 1: Batata Quente
def batata_quente(jogadores):
    lista = CircularLinkedList()
    for jogador in jogadores:
        lista.inserir_final(jogador)

    atual = lista.head
    while lista.contar_elementos() > 1:
        k = random.randint(1, 10)
        for _ in range(k - 1):
            atual = atual.next
        print(f"{atual.data} está com a batata quente e foi eliminado!")
        eliminado = atual.data
        atual = atual.next
        lista.remover(eliminado)
    print(f"O vencedor é {lista.head.data}!")

# Desafio 2: Batalha de Cavaleiros
def batalha_cavaleiros(nomes):
    class Cavaleiro:
        def __init__(self, nome):
            self.nome = nome
            self.hp = random.randint(50, 100)

        def __str__(self):
            return f"{self.nome} (HP: {self.hp})"

    lista = CircularLinkedList()
    for nome in nomes:
        lista.inserir_final(Cavaleiro(nome))

    atual = lista.head
    while lista.contar_elementos() > 1:
        atacante = atual.data
        defensor = atual.next.data
        dano = random.randint(5, 10)
        defensor.hp -= dano
        print(f"{atacante.nome} ataca {defensor.nome} causando {dano} de dano. HP restante: {defensor.hp}")
        if defensor.hp <= 0:
            print(f"{defensor.nome} foi eliminado!")
            eliminado = atual.next.data
            lista.remover(eliminado)
        atual = atual.next
    print(f"O campeão é {lista.head.data.nome} com {lista.head.data.hp} de HP!")
