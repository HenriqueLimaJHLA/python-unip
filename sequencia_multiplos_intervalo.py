def sequencia_multiplos_intervalo():
    intervalo_inicial = int(input("\nDigite o invervalo inicial: "))
    intervalo_final = int(input("Agora, digite o invervalo final: "))
    
    if intervalo_inicial > intervalo_final:
        print("\n----Error: Intervalo Inicial é maior que o Intervalo Final!!\n")
    else:
        numero = int(input("\nPor fim, digite um número qualquer (desde que esteja dentro desse intervalo): "))
        
        if numero >= intervalo_inicial and numero <= intervalo_final:
            for multiplos in range(intervalo_inicial, intervalo_final):
                if multiplos % numero == 0:
                    print(f"{multiplos} é Múltiplo de {numero}.")
                else:
                    print(f"{multiplos} Não é Múltiplo de {numero}.")
        else:
            print(f"\nNúmero não está dentro do intervalo dos números {intervalo_inicial} e {intervalo_final}.\n")
sequencia_multiplos_intervalo()