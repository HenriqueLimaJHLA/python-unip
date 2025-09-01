def numeros_em_ordem():
    lista_numeros = []

    for i in range(0, 3):
        i +=1
        numero = int(input(f"Digite o {i}º número: "))
        lista_numeros.append(numero)
    lista_numeros_ordenada = sorted(lista_numeros)
    print(f"\nNúmeros Ordenados: {lista_numeros_ordenada}\n")
numeros_em_ordem()