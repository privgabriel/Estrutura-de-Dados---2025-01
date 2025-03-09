class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def inserir(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # Faz a lista circular
        else:
            temp = self.head
            while temp.next != self.head:  # Percorre até o último nó
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # Fecha o ciclo

    def remover(self, data):
        if not self.head:
            return

        temp = self.head
        prev = None

        # Caso especial: Se o nó a ser removido for o único da lista
        if temp.data == data and temp.next == self.head:
            self.head = None
            return

        while True:
            if temp.data == data:  # Encontrou o nó a ser removido
                if prev:
                    prev.next = temp.next
                else:  # Removendo o nó cabeça
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    self.head = temp.next
                    last.next = self.head
                return
            prev = temp
            temp = temp.next

            if temp == self.head:  # Se percorreu toda a lista e não encontrou
                break

    def exibir(self):
        if not self.head:
            print("Lista vazia")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print(f"(volta para {self.head.data})")  # Indica que a lista é circular

# Exemplo de uso:
lista = CircularLinkedList()
lista.inserir("Info1")
lista.inserir("Info2")
lista.inserir("Info3")

print("Lista circular inicial:")
lista.exibir()

lista.remover("Info2")
print("\nLista após remover 'Info2':")
lista.exibir()
