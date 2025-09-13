def soma_inteiros():
    
    contador = 1
    soma_total = 0
    
    qtd_numeros = int(input("\nDigite a quantidade de números que irá digitar: "))
    
    while contador <= qtd_numeros:
        
        numero = int(input("\nDigite um número: "))
        soma_total += numero
        contador += 1
    
    print(f"\nSoma Total: {soma_total}\nQuantidade de Números: {qtd_numeros}\n")
soma_inteiros()