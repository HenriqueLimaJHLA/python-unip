def calcular_fatorial():
    numero = int(input(f"\nDigite um número para descobrir o seu fatorial: "))
    fatorial = 1

    print("")
    for i in range(numero, 0, -1):
        if fatorial != 1:
            print(f"{fatorial} * {i} = {fatorial * i}")
        fatorial *= i
    print(f"\nFatorial de {numero} é: {fatorial}\n")
calcular_fatorial()