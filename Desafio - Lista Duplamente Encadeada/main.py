import random

class Node:
    def __init__(self, atual):
        self.atual = atual
        self.proximo = None
        self.anterior = None

class ListaCircular:
    def __init__(self, quantidade):
        self.cabeca = None
        self.quantidade = quantidade
        self.criar_lista()

    def criar_lista(self):
        self.cabeca = Node(1)
        atual = self.cabeca
        for i in range(2, self.quantidade + 1):
            novo = Node(i)
            novo.anterior = atual
            atual.proximo = novo
            atual = novo
        atual.proximo = self.cabeca
        self.cabeca.anterior = atual
        self.cabeca.anterior.proximo = self.cabeca
        self.cabeca.anterior = atual

    def remover(self, no):
        no.anterior.proximo = no.proximo
        no.proximo.anterior = no.anterior
        if no == self.cabeca:
            self.cabeca = no.proximo
        return no.proximo

    def jogar(self):
        no = self.cabeca
        while self.quantidade > 1:
            passos = random.randint(1, self.quantidade * 2)
            for _ in range(passos):
                no = no.proximo
            print(f"Eliminado: {no.atual}")
            no = self.remover(no)
            self.quantidade -= 1
        print(f"🛡️ Sobrevivente: {no.atual}")

lista = ListaCircular(10)
lista.jogar()
