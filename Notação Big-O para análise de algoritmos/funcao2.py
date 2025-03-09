import timeit

def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

# print(lista1())

# tempo = timeit.timeit(lambda : lista1(), number=1)
# print(f"Tempo de execução: {tempo:.6f} segundos")

#MILIOR
def lista2():
    return range(1000)

tempo = timeit.timeit(lambda : lista2(), number=1)
print(f"Tempo de execução: {tempo:.6f} segundos")