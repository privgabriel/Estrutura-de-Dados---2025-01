class Lista:
    def __init__(self, info):
        self.info = info
        self.anterior = None
        self.prox = None

    def inserir_lista(self, valor):
        novo_elemento = Lista(valor)

        novo_elemento.prox = self  # O novo nó aponta para o nó atual
        self.anterior = novo_elemento  # O nó atual referencia o novo nó como "anterior"

        return novo_elemento  # Retorna o novo nó para atualização externa

    def print_list(self):
        atual = self
        while atual is not None:
            print(f'Valor atual {atual.info}')
            atual = atual.prox

    def remover_valor_lista(self, valor, lista):
        atual = lista

        # Se o primeiro nó for o que queremos remover
        if atual.info == valor:
            lista = atual.prox  # Atualiza a referência da lista para o próximo nó
            if lista is not None:
                lista.anterior = None  # Se houver um nó após o primeiro, atualiza o anterior
            return lista  # Retorna a nova referência da lista

        # Caso contrário, percorre a lista
        while atual is not None:
            if atual.info == valor:
                if atual.prox is not None:
                    atual.prox.anterior = atual.anterior  # O próximo nó aponta para o anterior
                if atual.anterior is not None:
                    atual.anterior.prox = atual.prox  # O nó anterior aponta para o próximo nó
                return lista  # Retorna a lista sem o nó removido
            atual = atual.prox

        print(f'Valor {valor} não encontrado.')
        return lista  # Retorna a lista sem alterações se o valor não foi encontrado


# Criando um primeiro nó na lista
minha_lista = Lista(1)

# Atualizando a referência para apontar para o novo primeiro nó
minha_lista = minha_lista.inserir_lista(5)

# Testando a estrutura da lista
print(minha_lista.info)  # Deve imprimir 5 (novo primeiro nó)
print(minha_lista.prox.info)  # Deve imprimir 1 (nó original)

# Exibindo a lista
minha_lista.print_list()

# Removendo um valor e exibindo a lista novamente
minha_lista = minha_lista.remover_valor_lista(5, minha_lista)
minha_lista.print_list()  # Deve imprimir apenas o valor 1
