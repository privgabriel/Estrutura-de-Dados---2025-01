class Pilha:
    def __init__(self):
        self.vetor = []

    def pilha_push(self, valor):
        self.vetor.append(valor)

    def pilha_pop(self):
        if not self.vetor:
            print("Nada para desfazer (pilha vazia)")
            return None
        return self.vetor.pop()

    def mostrar_texto(self):
        return ''.join(self.vetor)

editor = Pilha()

entrada = input("Digite o texto (use '#' para apagar o último caractere): ")

for caractere in entrada:
    if caractere == '#':
        editor.pilha_pop()
    else:
        editor.pilha_push(caractere)

print("\nTexto final:")
print(editor.mostrar_texto())
