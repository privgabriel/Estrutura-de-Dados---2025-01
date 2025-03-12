class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

    def insert_node(self, lista, valor):
        atual = lista
        while atual.prox is not None:
            atual = atual.prox

        novo_item = Lista(valor)
        atual.prox = novo_item

    def imprimir_lista(self, lista):
        atual = lista
        while atual.prox is not None:
            print(f"Valor Atual: {atual}")
            atual = atual.prox

    def buscar_lista(self, lista, valor):
        atual = lista

        while atual is not None:
            if atual.info == valor:
                return atual
        atual = atual.prox
        return None

    def remover_lista(self, lista, valor):
        atual = lista
        anterior = None

        while atual is not None:
            if atual.info == valor:
                if atual == lista:
                    return atual.prox
                elif atual.prox == None:
                    anterior.prox = None
                    return lista
                else:

                print(f"Removendo elemento... {valor}")
            atual = atual.prox





minha_lista = Lista(1)


minha_lista.insert_node(minha_lista, 2)
minha_lista.insert_node(minha_lista, 3)

minha_lista.imprimir_lista(minha_lista)

minha_lista.buscar_lista(minha_lista, 2)

minha_lista.remover_lista(minha_lista, 2)

minha_lista.imprimir_lista(minha_lista)
