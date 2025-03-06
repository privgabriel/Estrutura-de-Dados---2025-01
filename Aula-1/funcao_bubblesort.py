def bubblesort():
    vector = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    n = len(vector)
    for i in range(n - 1):
        for j in range(n - 1):
            print(f'Comparando {vector[j]} com {vector[j + 1]}')
            if vector[j] > vector[j + 1]:
                    vector[j], vector[j + 1] = vector[j + 1], vector[j]
                    print(f'Trocando {vector[j]} com {vector[j + 1]}')
    print(vector)
bubblesort()