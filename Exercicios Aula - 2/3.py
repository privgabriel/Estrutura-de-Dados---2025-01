class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    head = Node(0)  # Nó cabeça temporário
    current = head

    while l1 and l2:
        current.next = l1
        l1 = l1.next
        current = current.next

        current.next = l2
        l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return head.next  # Retorna a cabeça da lista intercalada

# Exemplo de uso
def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# Criando a primeira lista: 2.1 -> 4.5 -> 1.0
l1 = Node(2.1)
l1.next = Node(4.5)
l1.next.next = Node(1.0)

# Criando a segunda lista: 7.2 -> 3.1 -> 9.8
l2 = Node(7.2)
l2.next = Node(3.1)
l2.next.next = Node(9.8)

# Mesclar as listas
merged_list = merge(l1, l2)

# Exibir a lista resultante
print_list(merged_list)
