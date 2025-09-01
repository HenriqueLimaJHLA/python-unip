def somar_numeros():
    soma = 0
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    soma = n1 + n2
    
    if soma:
        print(f"A soma dos dois números é de: {soma}")
    return False

somar_numeros()