def sequencia_multiplos():
    numero = int(input("Digite um número: "))
    print("")

    if numero <= 0 or numero > 1000:
        print("Insira um número maior que 0 e menor que 1000.\n")
    else:        
        for numeros_multiplos in range(1, 1001):
            if numeros_multiplos % numero == 0:
                print(f"{numeros_multiplos} é múltiplo do número {numero}.")
sequencia_multiplos()