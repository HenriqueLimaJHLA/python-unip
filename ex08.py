import os as Os

def calcular_quantidade_caixas():
    # Variáveis
    qtd_caixas_totais = 0
    qtd_caixas_caminhao = 0
    qtd_viagens = 0
    qtd_viagens_restantes = 0
    
    # Inputs
    qtd_caixas_totais = int(input("\nDigite a quantidade de caixas totais: "))
    qtd_caixas_caminhao = int(input("Digite a quantidade de caixas que esse caminhão suporta por viagem: "))
    
    qtd_viagens = qtd_caixas_totais // qtd_caixas_caminhao
    qtd_viagens_restantes = qtd_caixas_totais % qtd_caixas_caminhao
    
    if qtd_viagens_restantes > 0: 
        print(f"\nQuantidade de viagens totais: {qtd_viagens} viagens. \nQuantidade iguais de caixas nas viagens: {qtd_caixas_caminhao} caixas. \nQuantidade de caixas na viagem a mais ({qtd_viagens+1} viagens): {qtd_viagens_restantes} caixas.\n")
    else:
        print(f"\nQuantidade de viagens totais: {qtd_viagens} viagens iguais. \nQuantidade de caixas levadas igualmente em cada viagem: {qtd_caixas_caminhao} caixas.\n")
        
    user_continue = str(input((f"\nDeseja Calcular novamente? [S/N]: ")))
    if user_continue in ["Sim", "S", "s", "Yes", "Y", "Si"]:
        Os.system('cls')
        calcular_quantidade_caixas()
    else:
        SystemExit()
calcular_quantidade_caixas() 