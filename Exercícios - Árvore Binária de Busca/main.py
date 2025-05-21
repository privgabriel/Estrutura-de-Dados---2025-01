class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        def _inserir(no, valor):
            if no is None:
                return No(valor)
            if valor < no.valor:
                no.esquerda = _inserir(no.esquerda, valor)
            elif valor > no.valor:
                no.direita = _inserir(no.direita, valor)
            return no
        self.raiz = _inserir(self.raiz, valor)

    def buscar(self, valor):
        def _buscar(no, valor):
            if no is None:
                return False
            if valor == no.valor:
                return True
            elif valor < no.valor:
                return _buscar(no.esquerda, valor)
            else:
                return _buscar(no.direita, valor)
        return _buscar(self.raiz, valor)

    def remover(self, valor):
        def _minimo_no(no):
            atual = no
            while atual.esquerda is not None:
                atual = atual.esquerda
            return atual

        def _remover(no, valor):
            if no is None:
                return no
            if valor < no.valor:
                no.esquerda = _remover(no.esquerda, valor)
            elif valor > no.valor:
                no.direita = _remover(no.direita, valor)
            else:
                if no.esquerda is None:
                    return no.direita
                elif no.direita is None:
                    return no.esquerda
                temp = _minimo_no(no.direita)
                no.valor = temp.valor
                no.direita = _remover(no.direita, temp.valor)
            return no

        self.raiz = _remover(self.raiz, valor)

    def pre_ordem(self):
        def _pre_ordem(no):
            if no:
                print(no.valor, end=' ')
                _pre_ordem(no.esquerda)
                _pre_ordem(no.direita)
        _pre_ordem(self.raiz)
        print()

    def in_ordem(self):
        def _in_ordem(no):
            if no:
                _in_ordem(no.esquerda)
                print(no.valor, end=' ')
                _in_ordem(no.direita)
        _in_ordem(self.raiz)
        print()

    def pos_ordem(self):
        def _pos_ordem(no):
            if no:
                _pos_ordem(no.esquerda)
                _pos_ordem(no.direita)
                print(no.valor, end=' ')
        _pos_ordem(self.raiz)
        print()


# Exemplo de uso:
if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()
    elementos = [50, 30, 20, 40, 70, 60, 80]
    for elem in elementos:
        arvore.inserir(elem)

    print("Em ordem:")
    arvore.in_ordem()

    print("Pré-ordem:")
    arvore.pre_ordem()

    print("Pós-ordem:")
    arvore.pos_ordem()

    print("Busca por 40:", arvore.buscar(40))
    print("Removendo 30...")
    arvore.remover(30)
    print("Em ordem após remoção:")
    arvore.in_ordem()
