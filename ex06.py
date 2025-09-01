def calcular_altura_ideal():
    altura = 0.00
    
    altura = float(input("Digite a sua altura (m) ou (cm): "))
    
    if altura > 2.5:
        altura /= 100
        
    formula_peso_ideal = (72.5 * altura) - 58.0
    print(f"O peso ideal para a altura {altura} m é de: {formula_peso_ideal} KG.")
    
calcular_altura_ideal()