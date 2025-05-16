# Classe que representa um nó da árvore
class No:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave         # Valor armazenado no nó
        self.esquerda = esquerda   # Filho à esquerda
        self.direita = direita     # Filho à direita

    def __repr__(self):
        # Representação do nó para impressão
        return '%s <- %s -> %s' % (
            self.esquerda and self.esquerda.chave,
            self.chave,
            self.direita and self.direita.chave
        )

# Classe que representa a Árvore Binária
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # A árvore começa sem nenhum nó

# Função para inserir um valor na árvore
def inserir(raiz, chave):
    if raiz is None:
        return No(chave)  # Se a raiz for nula, cria um novo nó
    if chave < raiz.chave:
        # Se a chave for menor, insere na subárvore esquerda
        raiz.esquerda = inserir(raiz.esquerda, chave)
    else:
        # Caso contrário, insere na subárvore direita
        raiz.direita = inserir(raiz.direita, chave)
    return raiz  # Retorna a raiz atualizada

# Função para remover um valor da árvore
def remover(raiz, chave):
    if raiz is None:
        return None  # Se a árvore estiver vazia, retorna None

    if chave < raiz.chave:
        # Se a chave for menor, busca na subárvore esquerda
        raiz.esquerda = remover(raiz.esquerda, chave)
    else:
        # Caso contrário, busca na subárvore direita
        raiz.direita = remover(raiz.direita, chave)

    if raiz.chave == chave:
        # Encontrou o nó a ser removido
        if raiz.esquerda is None and raiz.direita is None:
            # Caso 1: é uma folha (sem filhos)
            print("O valor a ser removido é uma folha!")
            raiz = None
        elif raiz.esquerda is None:
            # Caso 2: tem apenas filho à direita
            raiz = raiz.direita
        elif raiz.direita is None:
            # Caso 3: tem apenas filho à esquerda
            raiz = raiz.esquerda
        else:
            # Caso 4: tem dois filhos
            # Substitui pelo maior valor da subárvore esquerda
            auxiliar = raiz.esquerda
            while auxiliar.direita is not None:
                auxiliar = auxiliar.direita

            # Troca os valores
            auxiliar.chave, raiz.chave = raiz.chave, auxiliar.chave

            # Remove o valor duplicado da subárvore esquerda
            raiz.esquerda = remover(raiz.esquerda, chave)

    return raiz  # Retorna a raiz atualizada

# Exemplo de uso
arvore = ArvoreBinaria()
arvore.raiz = No(5)
inserir(arvore.raiz, 2)
inserir(arvore.raiz, 6)

print("Antes da remoção:")
print(arvore.raiz)

remover(arvore.raiz, 2)

print("Depois da remoção:")
print(arvore.raiz)
