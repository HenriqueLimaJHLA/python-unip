def soma_numero():
    contador = 1
    soma_total = 0
    
    numero = int(input("Digite um número: "))
    
    while contador <= numero:
        soma_total += contador
        contador += 1

    print(f"Soma Total: {soma_total}")
soma_numero()