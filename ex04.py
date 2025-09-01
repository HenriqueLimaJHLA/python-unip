import datetime

def calcular_idade():
    idade = 0
    data_atual = datetime.date.today()
    
    dia_nascimento = int(input("Digite o dia do seu Nascimento: "))
    mes_nascimento = int(input("Digite o mês do seu Nascimento: "))
    ano_nascimento = int(input("Digite o ano do seu Nascimento: "))
    
    data_nascimento = datetime.date(day=dia_nascimento, month=mes_nascimento, year=ano_nascimento)
    
    if data_nascimento >= data_atual:
        return 0
    
    idade = data_atual - data_nascimento
    idade /= 365
    print(f"Você possui: {idade.days} anos!")

calcular_idade()