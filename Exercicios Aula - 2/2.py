#Considere listas de valores inteiros e implemente uma função que receba
#como parâmetro uma lista encadeada e um valor inteiro n e divida a lista em
#duas, de forma a segunda lista começar no primeiro nó logo após a
#ocorrência de n na lista original. A figura a seguir ilustra esta separação:

class Lista:
    def __init__(self):
        self.lista = []

    def divide(self, lista, n):
        if n in lista:  # Verifica se n existe na lista
            indice = lista.index(n) 
            return lista[indice + 1:]  # Retorna a lista a partir do próximo elemento
        return [] 

    def ler(self, lista):
        for item in lista:
            print(item)

lista = Lista()
lista.lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
n = 5
lista.ler(lista.divide(lista.lista, n))

