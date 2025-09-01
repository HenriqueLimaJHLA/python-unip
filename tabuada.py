def tabuada_numeros():
    numero_tabuada = 0
    numero_tabuada = int(input(f"\nDigite um número para saber a sua tabuada: "))

    for i in range(0,11):
        resultado = i * numero_tabuada
        print(f"{i} * {numero_tabuada} = {resultado}")
tabuada_numeros()