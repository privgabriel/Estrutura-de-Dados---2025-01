vetor = [1, 2, 3, 4, 5]
maior = vetor[0]
menor = vetor[0]

for valor in vetor:
    if valor > maior:
        maior = valor
    else:
        menor = valor

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")    