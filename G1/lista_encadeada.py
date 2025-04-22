class Lista:
    def __init__(self, valor_atual=None):
        self.valor_atual = valor_atual
        self.proximo = None

    @staticmethod
    def criar_lista():
        return None
    
    @staticmethod
    def inserir_na_lista(lista, valor):
        novo_valor = Lista(valor)
        novo_valor.proximo = lista
        return novo_valor
    
    @staticmethod
    def lista_imprimir(lista):
        atual = lista
        while atual is not None:
            print(atual.valor_atual)
            atual = atual.proximo

# Criar lista vazia
minha_lista = Lista.criar_lista()

# Inserir elementos (vai inserindo no início)
minha_lista = Lista.inserir_na_lista(minha_lista, 10)
minha_lista = Lista.inserir_na_lista(minha_lista, 20)
minha_lista = Lista.inserir_na_lista(minha_lista, 30)

# Imprimir lista
Lista.lista_imprimir(minha_lista)

