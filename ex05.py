def calcular_salario():
    salario = 0.00
    
    valor_salario_hora = float(input("Digite o salário ganhado por hora: "))
    horas_trabalhadas_dias = int(input("Quantas horas trabalhadas por dia?: "))
    
    if valor_salario_hora == 0 | horas_trabalhadas_dias == 0:
        return False
    
    salario = valor_salario_hora * (horas_trabalhadas_dias * 30)
    
    print(f"O seu salário por mês é de: R$ {salario}")
    
calcular_salario()