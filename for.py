def lista():
    lista_numeros = [2, 5, 7, 3, 8, 10]
    soma_numeros = 0

    print("")

    for numero in lista_numeros:
        print(f"Somas: {soma_numeros} + {numero} = {soma_numeros + numero}")
        soma_numeros += numero
    print(f"\nTotal: {soma_numeros}\n")
lista()