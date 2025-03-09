class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def copia(lst):
    if not lst:
        return None  # Retorna None se a lista original estiver vazia

    head = Node(lst.data)  # Cria o primeiro nó da nova lista
    current_original = lst.next
    current_copy = head

    while current_original:
        current_copy.next = Node(current_original.data)  # Cria um novo nó com os mesmos dados
        current_copy = current_copy.next
        current_original = current_original.next

    return head  # Retorna a cópia da lista

# Função para criar uma lista a partir de um array
def create_list(elements):
    if not elements:
        return None
    head = Node(elements[0])
    current = head
    for element in elements[1:]:
        current.next = Node(element)
        current = current.next
    return head

# Função para imprimir a lista
def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# Criando uma lista de teste
original_list = create_list(["alpha", "beta", "gamma"])

# Fazendo a cópia
copied_list = copia(original_list)

# Exibir listas
print("Lista original:")
print_list(original_list)

print("Lista copiada:")
print_list(copied_list)
