class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def inverte(lst):
    prev = None
    current = lst

    while current:
        next_node = current.next  # Guarda a referência do próximo nó
        current.next = prev  # Inverte a direção do ponteiro
        prev = current  # Atualiza o anterior para o nó atual
        current = next_node  # Avança para o próximo nó

    return prev  # Retorna a nova cabeça da lista invertida

# Exemplo de uso
def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# Criando a lista original: 2.1 -> 4.5 -> 1.0 -> 7.2 -> 9.8
lst = Node(2.1)
lst.next = Node(4.5)
lst.next.next = Node(1.0)
lst.next.next.next = Node(7.2)
lst.next.next.next.next = Node(9.8)

print("Lista Original:")
print_list(lst)

# Inverter a lista
reversed_lst = inverte(lst)

print("Lista Invertida:")
print_list(reversed_lst)
