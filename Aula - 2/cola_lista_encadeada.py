class No:
    """Classe que representa um nó de uma lista encadeada."""
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaEncadeada:
    """Classe que representa uma lista encadeada e suas operações."""
    
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        """Insere um valor no início da lista."""
        novo_no = No(valor)
        novo_no.prox = self.inicio
        self.inicio = novo_no

    def inserir_final(self, valor):
        """Insere um valor no final da lista."""
        novo_no = No(valor)
        if not self.inicio:
            self.inicio = novo_no
            return
        atual = self.inicio
        while atual.prox:
            atual = atual.prox
        atual.prox = novo_no

    def imprimir(self):
        """Imprime os elementos da lista."""
        atual = self.inicio
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.prox
        print("None")

    def list_comprimento(self):
        """Retorna o número de elementos da lista."""
        atual = self.inicio
        tamanho = 0
        while atual:
            tamanho += 1
            atual = atual.prox
        return tamanho

    def maiores(self, n):
        """Conta quantos elementos são maiores que n."""
        atual = self.inicio
        contador = 0
        while atual:
            if atual.valor > n:
                contador += 1
            atual = atual.prox
        return contador

    def ultimo(self):
        """Retorna o último nó da lista."""
        if not self.inicio:
            return None
        atual = self.inicio
        while atual.prox:
            atual = atual.prox
        return atual

    def concatena(self, outra_lista):
        """Concatena duas listas encadeadas."""
        if not self.inicio:
            self.inicio = outra_lista.inicio
            return
        atual = self.inicio
        while atual.prox:
            atual = atual.prox
        atual.prox = outra_lista.inicio

    def lista_calcula_media(self):
        """Calcula a média dos valores da lista."""
        if not self.inicio:
            return 0
        soma = 0
        contador = 0
        atual = self.inicio
        while atual:
            soma += atual.valor
            contador += 1
            atual = atual.prox
        return soma / contador

    def lista_altera(self):
        """Altera os valores para seus opostos (positivo ↔ negativo)."""
        atual = self.inicio
        while atual:
            atual.valor *= -1
            atual = atual.prox

    def lista_retira_ant(self, v):
        """Remove o elemento anterior ao primeiro nó que contém o valor v."""
        if not self.inicio or not self.inicio.prox:
            return
        
        if self.inicio.prox.valor == v:
            self.inicio = self.inicio.prox
            return

        anterior = None
        atual = self.inicio

        while atual.prox and atual.prox.valor != v:
            anterior = atual
            atual = atual.prox

        if atual.prox:
            anterior.prox = atual.prox  # Remove o nó anterior ao v

    def retira_n(self, n):
        """Remove todas as ocorrências de n da lista."""
        while self.inicio and self.inicio.valor == n:
            self.inicio = self.inicio.prox
        
        atual = self.inicio
        while atual and atual.prox:
            if atual.prox.valor == n:
                atual.prox = atual.prox.prox
            else:
                atual = atual.prox

    def inverte(self):
        """Inverte a ordem da lista encadeada."""
        anterior = None
        atual = self.inicio
        while atual:
            prox = atual.prox
            atual.prox = anterior
            anterior = atual
            atual = prox
        self.inicio = anterior

    def copia(self):
        """Cria uma cópia da lista encadeada."""
        if not self.inicio:
            return None
        nova_lista = ListaEncadeada()
        atual = self.inicio
        while atual:
            nova_lista.inserir_final(atual.valor)
            atual = atual.prox
        return nova_lista

    def igual(self, outra_lista):
        """Verifica se duas listas são iguais."""
        atual1 = self.inicio
        atual2 = outra_lista.inicio
        while atual1 and atual2:
            if atual1.valor != atual2.valor:
                return False
            atual1 = atual1.prox
            atual2 = atual2.prox
        return atual1 is None and atual2 is None

    def merge(self, outra_lista):
        """Intercala os elementos de duas listas."""
        nova_lista = ListaEncadeada()
        atual1 = self.inicio
        atual2 = outra_lista.inicio

        while atual1 or atual2:
            if atual1:
                nova_lista.inserir_final(atual1.valor)
                atual1 = atual1.prox
            if atual2:
                nova_lista.inserir_final(atual2.valor)
                atual2 = atual2.prox

        return nova_lista
    
# Criando listas
lista1 = ListaEncadeada()
lista1.inserir_final(1)
lista1.inserir_final(2)
lista1.inserir_final(3)
lista1.inserir_final(4)
lista1.inserir_final(5)

lista2 = ListaEncadeada()
lista2.inserir_final(10)
lista2.inserir_final(20)

print("Lista 1:")
lista1.imprimir()

print("Comprimento da lista:", lista1.list_comprimento())
print("Elementos maiores que 2:", lista1.maiores(2))
print("Último elemento:", lista1.ultimo().valor)
print("Média da lista:", lista1.lista_calcula_media())

# Removendo um número específico
lista1.retira_n(3)
print("Lista após remover 3:")
lista1.imprimir()

# Invertendo a lista
lista1.inverte()
print("Lista invertida:")
lista1.imprimir()

# Alternando sinais
lista1.lista_altera()
print("Lista com sinais invertidos:")
lista1.imprimir()

# Concatenando listas
lista1.concatena(lista2)
print("Lista 1 concatenada com Lista 2:")
lista1.imprimir()

# Criando cópia
lista_copia = lista1.copia()
print("Cópia da lista 1:")
lista_copia.imprimir()

# Comparando listas
print("As listas são iguais?", lista1.igual(lista_copia))

# Intercalando listas (merge)
lista_merge = lista1.merge(lista2)
print("Lista mesclada:")
lista_merge.imprimir()

