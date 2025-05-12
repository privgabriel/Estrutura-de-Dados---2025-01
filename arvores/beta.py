class No:
    def __init__(self, valor=None, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

def inserir(raiz, valor):
    if raiz is None:
        return No(valor)
    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    else:
        raiz.direita = inserir(raiz.direita, valor)
    return raiz

raiz = None
raiz = inserir(raiz, 5)
raiz = inserir(raiz, 3)
raiz = inserir(raiz, 10)

# Impressão com verificação se esquerda e direita existem
print(f'{raiz.esquerda.valor if raiz.esquerda else "None"} <- {raiz.valor} -> {raiz.direita.valor if raiz.direita else "None"}')
