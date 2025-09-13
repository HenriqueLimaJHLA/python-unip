def isprimo():
    contador = 2
    primo = False
    
    numero = int(input("\nDigite um número: "))
    
    if numero <= 1:
        print("Numero não é primo!\n")
    else:      
        while contador <= (numero - 1) and not primo:
            resto = numero % contador
    
            if resto == 0: primo = True
        
            contador += 1
        
        if not primo: print(f"{numero} é um número primo!\n")
        else: print(f"{numero} não é um número primo!\n")            
isprimo()
