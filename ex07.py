def calcular_salario_imposto():
    salario = 0.00
    # desconto_inss = 0.08
    # desconto_fgts = 0.11
    
    valor_salario_hora = float(input("Digite o salário ganhado por hora: "))
    horas_trabalhadas_mes = int(input("Quantas horas trabalhadas por mês?: "))
    
    if valor_salario_hora == 0 | horas_trabalhadas_mes == 0:
        return False
    
    salario = valor_salario_hora * horas_trabalhadas_mes 
    
    print(f"O seu salário por mês é de: R$ {salario}")
    
calcular_salario_imposto()