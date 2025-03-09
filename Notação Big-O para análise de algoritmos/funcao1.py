import timeit
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    print(soma)
    return soma
    
# tempo = timeit.timeit(lambda: soma1(10), number=1)
# print(f"Tempo de execução: {tempo:.6f} segundos")


#MILIOR
def soma2(n):
    return (n * (n + 1) / 2)

tempo2 = timeit.timeit(lambda: soma2(10), number= 1)
print(f"Tempo de execução: {tempo2:.6f} segundos")
