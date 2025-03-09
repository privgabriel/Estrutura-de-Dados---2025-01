class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def igual(l1, l2):
    while l1 and l2:
        if l1.data != l2.data:  # Se os dados dos nós forem diferentes
            return False
        l1 = l1.next
        l2 = l2.next
    
    return l1 is None and l2 is None  # Verifica se ambas terminaram ao mesmo tempo

# Exemplo de uso
def create_list(elements):
    if not elements:
        return None
    head = Node(elements[0])
    current = head
    for element in elements[1:]:
        current.next = Node(element)
        current = current.next
    return head

# Criando listas de teste
l1 = create_list(["a", "b", "c"])
l2 = create_list(["a", "b", "c"])
l3 = create_list(["a", "b", "d"])
l4 = create_list(["a", "b", "c", "d"])

# Testando a função
print(igual(l1, l2))  # True (listas iguais)
print(igual(l1, l3))  # False (conteúdo diferente)
print(igual(l1, l4))  # False (tamanhos diferentes)
