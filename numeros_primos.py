def numeros_primos():
    numero = int(input("Digite um número: "))
    qtd_divisores = 0
    divisores = []
    for i in range(1,101):
        if numero % i == 0:
            divisores.append(i)
            qtd_divisores += 1
            
    if qtd_divisores == 2 or numero == 2:
        print(f"O Número {numero} é Primo! Apenas {qtd_divisores} divisores: {divisores}") 
    else:
        print(f"O Número {numero} não é Primo! Ele possui {qtd_divisores} divisores: {divisores}")         
        
numeros_primos()