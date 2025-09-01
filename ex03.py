def calcular_area_circunferencia():
    area = 0
    tamanho_pi = 3.14
    
    raio = float(input("Digite o tamanho do raio (cm): "))
    
    if (raio == 0):
        return area
    
    area = tamanho_pi*(raio**2)
    print(f"O tamanho da área da circunferência é de: {area} cm².")
    
calcular_area_circunferencia()