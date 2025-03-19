class ListasDuplamenteEncadeadas:
    def __init__(self, info):
        self.info = info
        self.anterior = None
        self.prox = None

    def inserir_na_lista(self, valor):
        novo_elemento = ListasDuplamenteEncadeadas(valor)  # Cria o novo nó
        atual = self  # Começa pelo nó atual

        # Percorre até o último nó da lista
        while atual.prox is not None:
            atual = atual.prox
        
        # Insere o novo nó no final
        atual.prox = novo_elemento
        novo_elemento.anterior = atual  # Liga o novo nó ao anterior

        return novo_elemento  # Retorna o novo nó inserido

    def imprimir_lista(self):
        atual = self  # Começa no primeiro nó

        while atual is not None:
            print(f'Valor atual: {atual.info}')
            atual = atual.prox  # Avança para o próximo nó

    def busca_valor(self, valor):
        atual = self  # Começa no primeiro nó

        while atual is not None:
            if atual.info == valor:
                print(f'Valor {valor} encontrado.')
                return True  # Retorna True se encontrado
            atual = atual.prox

        print(f'Valor {valor} não encontrado.')
        return False  # Retorna False se não encontrado
    
    
    def remover_valor_lista(self, valor):
        atual = self  # Começa no primeiro nó

        # Se o primeiro nó for o valor a ser removido
        if atual.info == valor:
            if atual.prox is not None:
                atual.prox.anterior = None  # Remove referência do próximo nó
                return atual.prox  # Retorna o próximo nó como a nova cabeça da lista
            else:
                return None  # Se só há um nó na lista, retorna None (lista vazia)

        while atual is not None:
            if atual.info == valor:
                print(f'Valor {valor} removido.')
                
                # Se for um nó do meio ou do fim
                if atual.anterior is not None:
                    atual.anterior.prox = atual.prox

                if atual.prox is not None:
                    atual.prox.anterior = atual.anterior

                return self  # Retorna a cabeça da lista sem o nó removido
            
            atual = atual.prox
        
        print(f'Valor {valor} não encontrado.')
        return self  # Retorna a lista sem alterações
    
    def inserir_fim_da_lista(self, valor):
        novo_elemento = ListasDuplamenteEncadeadas(valor)
        atual = self

        while atual.prox is not None:
            atual = atual.prox

        atual.prox = novo_elemento
        novo_elemento.anterior = atual

        return novo_elemento
    
    def inserir_ordenado(self, valor):
        novo_elemento = ListasDuplamenteEncadeadas(valor)
        atual = self

        while atual.prox is not None:
            if atual.info < valor:
                atual = atual.prox
            else:
                novo_elemento.prox = atual
                novo_elemento.anterior = atual.anterior
                atual.anterior.prox = novo_elemento
                atual.anterior = novo_elemento
                return novo_elemento

        atual.prox = novo_elemento
        novo_elemento.anterior = atual

        return novo_elemento



# Criando a lista e inserindo valores
minha_lista = ListasDuplamenteEncadeadas(1)
minha_lista.inserir_na_lista(5)
minha_lista.inserir_na_lista(10)
minha_lista.inserir_na_lista(15)
minha_lista.busca_valor(10)
minha_lista.remover_valor_lista(10)
minha_lista.inserir_fim_da_lista(20)
minha_lista.inserir_ordenado(8)
minha_lista.imprimir_lista()