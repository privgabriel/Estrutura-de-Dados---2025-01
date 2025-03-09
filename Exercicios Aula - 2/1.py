#Considere listas de valores inteiros e implemente uma função que receba
#como parâmetros uma lista encadeada e um valor inteiro n, retire da lista
#todas as ocorrências de n e retorne a lista resultante. Esta função deve
#obedecer ao protótipo:

class Listas:
    def __init__(self):
        self.lista = []

    def remove(self, lista, n):
        return [x for x in lista if x != n]  # Cria uma nova lista sem os elementos n

    def ler(self, lista):
        for item in lista:
            print(item)

lista = Listas()
lista.lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
n = 5
lista.ler(lista.remove(lista.lista, n))


