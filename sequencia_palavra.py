def sequencia():
    palavra = str(input("Digite uma palavra: "))
    letras = 0

    for palavras in palavra:
        letras+=1
        print(palavras, end=" ")
        
    print(f"\nQuantidade de Letras: {letras}")
sequencia()