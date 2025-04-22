class Aluno:
    def __init__(self, matricula, p1, p2, p3):
        self.matricula = matricula
        self.notas = [p1, p2, p3]
        self.prox = None

    def media(self):
        return sum(self.notas) / 3


def insere_ordenado(lista, matricula, p1, p2, p3):
    novo = Aluno(matricula, p1, p2, p3)

    # Caso a lista esteja vazia ou o novo tem média maior que o primeiro
    if lista is None or novo.media() > lista.media():
        novo.prox = lista
        return novo

    # Percorre até achar a posição correta
    atual = lista
    while atual.prox is not None and atual.prox.media() >= novo.media():
        atual = atual.prox

    novo.prox = atual.prox
    atual.prox = novo
    return lista


def imprimir_lista(lista):
    atual = lista
    while atual is not None:
        print(f"Matrícula: {atual.matricula}, Média: {atual.media():.2f}")
        atual = atual.prox


# 🔽 Exemplo com 4 inserções
lista_alunos = None

lista_alunos = insere_ordenado(lista_alunos, 1001, 8.0, 7.5, 9.0)
lista_alunos = insere_ordenado(lista_alunos, 1002, 6.0, 5.0, 7.0)
lista_alunos = insere_ordenado(lista_alunos, 1003, 9.5, 9.0, 10.0)
lista_alunos = insere_ordenado
