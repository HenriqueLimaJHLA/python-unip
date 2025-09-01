def dias_da_semana():
    dia_semana = 0

    dia_semana = int(input("Digite um dia da semana de 1 a 7: "))
    
    if dia_semana == 0:
        print("Dia inválido")
    elif dia_semana == 1:
        print("Domingo")
    elif dia_semana == 2:
        print("Segunda")
    elif dia_semana == 3:
        print("Terça")
    elif dia_semana == 4:
        print("Quarta")
    elif dia_semana == 5:
        print("Quinta")
    elif dia_semana == 6:
        print("Sexta")
    elif dia_semana == 7:
        print("Sábado")
            
    
dias_da_semana()