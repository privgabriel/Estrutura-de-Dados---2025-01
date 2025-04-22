def ordenar_vetor_bubble_sort(lista_de_numeros):
    tamanho_lista = len(lista_de_numeros)

    for numero_da_passagem in range(tamanho_lista):
        print(f"\n🔁 Passagem {numero_da_passagem + 1}:")
        
        # A cada passagem, o maior número vai para o final da "parte não ordenada"
        for indice_atual in range(0, tamanho_lista - numero_da_passagem - 1):
            numero_atual = lista_de_numeros[indice_atual]
            proximo_numero = lista_de_numeros[indice_atual + 1]

            print(f"  ➡️ Comparando {numero_atual} com {proximo_numero}")

            # Se o número atual for maior que o próximo, trocamos eles de lugar
            if numero_atual > proximo_numero:
                print(f"  🔄 Trocando {numero_atual} com {proximo_numero}")
                lista_de_numeros[indice_atual], lista_de_numeros[indice_atual + 1] = proximo_numero, numero_atual
            
            print("  📊 Estado atual da lista:", lista_de_numeros)
    
    return lista_de_numeros

meu_vetor = [5, 1, 4, 2, 8]
print("📦 Vetor original:", meu_vetor)

vetor_ordenado = ordenar_vetor_bubble_sort(meu_vetor)
print("\n✅ Vetor ordenado:", vetor_ordenado)

