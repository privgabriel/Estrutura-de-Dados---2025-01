class ListasDuplamenteEncadeadasCirculares:
    def __init__(self, info):
        self.info = info
        self.anterior = self  # Aponta para si mesmo
        self.prox = self  # Aponta para si mesmo

    def inserir_na_lista(self, valor):
        novo_elemento = ListasDuplamenteEncadeadasCirculares(valor)
        ultimo = self.anterior  # Obtém o último nó
        
        ultimo.prox = novo_elemento
        novo_elemento.anterior = ultimo
        novo_elemento.prox = self
        self.anterior = novo_elemento
        
        return novo_elemento

    def imprimir_lista(self):
        atual = self
        print(f'Valor atual: {atual.info}')
        atual = atual.prox
        while atual != self:
            print(f'Valor atual: {atual.info}')
            atual = atual.prox

    def busca_valor(self, valor):
        atual = self
        if atual.info == valor:
            print(f'Valor {valor} encontrado.')
            return True
        atual = atual.prox
        while atual != self:
            if atual.info == valor:
                print(f'Valor {valor} encontrado.')
                return True
            atual = atual.prox
        print(f'Valor {valor} não encontrado.')
        return False

    def remover_valor_lista(self, valor):
        atual = self
        while True:
            if atual.info == valor:
                if atual.prox == atual:
                    return None  # Único elemento na lista
                atual.anterior.prox = atual.prox
                atual.prox.anterior = atual.anterior
                return self if atual != self else atual.prox
            atual = atual.prox
            if atual == self:
                break
        print(f'Valor {valor} não encontrado.')
        return self

    def inserir_fim_da_lista(self, valor):
        return self.inserir_na_lista(valor)
    
    def inserir_ordenado(self, valor):
        novo_elemento = ListasDuplamenteEncadeadasCirculares(valor)
        atual = self
        
        while atual.prox != self and atual.prox.info < valor:
            atual = atual.prox
        
        novo_elemento.prox = atual.prox
        novo_elemento.anterior = atual
        atual.prox.anterior = novo_elemento
        atual.prox = novo_elemento
        
        return novo_elemento
    
    def imprimir_lista_inversa(self):
        atual = self.anterior
        print(f'Valor atual: {atual.info}')
        atual = atual.anterior
        while atual != self.anterior:
            print(f'Valor atual: {atual.info}')
            atual = atual.anterior


# Criando a lista circular e inserindo valores
minha_lista = ListasDuplamenteEncadeadasCirculares(1)
minha_lista.inserir_na_lista(5)
minha_lista.inserir_na_lista(10)
minha_lista.inserir_na_lista(15)
minha_lista.busca_valor(10)
minha_lista = minha_lista.remover_valor_lista(10)
minha_lista.inserir_fim_da_lista(20)
minha_lista.inserir_ordenado(8)
print("Impressão normal:")
minha_lista.imprimir_lista()
print("Impressão inversa:")
minha_lista.imprimir_lista_inversa()