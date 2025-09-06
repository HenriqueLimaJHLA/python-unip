def palavras_funcao():
    qtd_vogais = 0
    
    palavra = input(f"\nDigite uma palavra: ")
    while len(palavra) == 0:
        palavra = input(f"\nNão pode ser vazio! Digite uma palavra: ")
    if len(palavra) > 0 and len(palavra) < 2:
        print("Erro: isto é uma letra!!")
    else:
        for letras in palavra:
            if letras in ["a", "e", "i", "o", "u"]:
                qtd_vogais += 1
        print(f"A palavra {palavra} possui {qtd_vogais} Vogais!\n")
palavras_funcao()