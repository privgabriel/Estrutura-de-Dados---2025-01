def vector_par():
    vector = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(len(vector)):
        if vector[i] % 2 == 0:
            print(f'{vector[i]} é par')
vector_par()