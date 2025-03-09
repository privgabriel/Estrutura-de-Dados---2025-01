import numpy as np
class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = - 1
        self.valores = np.empty(self.capacidade, dtype=int)

    #Impressão O(n)
    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'{i} - {self.valores[i]}')
    #Inserção O(1) - O(2)
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade Máxima atingida")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    #Pesquisa Posição O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                print(f'Valor {valor} encontrado na posição {i}')
                return i
        return print('Valor não encontrado')

    #Exclusão O(n)
    def exluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == - 1:
            print("Não é possivel excluir o vetor")
            return - 1
        else:
            for i in range(posicao , self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1



vetor = VetorNaoOrdenado(5)
vetor.inserir(2)
vetor.inserir(3)
vetor.inserir(5)
vetor.inserir(8)
vetor.inserir(1)
vetor.inserir(7) #Capacidade Máxima atingida
vetor.imprimir()
vetor.pesquisar(2)
vetor.exluir(5)
vetor.imprimir()
vetor.exluir(2)
vetor.imprimir()
vetor.inserir(40)
vetor.imprimir()