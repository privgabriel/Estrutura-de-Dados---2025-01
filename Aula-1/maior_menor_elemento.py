def maior_menor_elemento():
    vector = [ 9, 8, 7, 6, 5, 4, 3, 2, 1]
    maior = vector[0]
    menor = vector[0]

    for i in range(len(vector)):
        if vector[i] > maior:
            maior = vector[i]
        if vector[i] < menor:
            menor = vector[i]
    print(f'O maior elemento é {maior}')
    print(f'O menor elemento é {menor}')

maior_menor_elemento()