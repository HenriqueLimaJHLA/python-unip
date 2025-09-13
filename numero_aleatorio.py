import random as Random 

def gerar_numero_aleatorio():
    numero_aleatorio_escolhido = Random.randint(1,100)
    chances = 5

    while chances > 0:
            numero_usuario = int(input(f"Digite um número tente adivinhar o número aleatório sorteado: "))
            chances -= 1
            
            if numero_usuario < 1 or numero_usuario > 100:
                chances += 1     
                print(f"\nDigite números apenas entre o intervalo [1..100]!!\nChances: {chances}\n")
            elif numero_usuario < numero_aleatorio_escolhido:
                print(f"\nNúmero inserido é menor que o número sorteado!")
                print(f"Chances: {chances}\n")
            elif numero_usuario > numero_aleatorio_escolhido:
                print(f"\nNúmero inserido é maior que o número sorteado!")
                print(f"Chances: {chances}\n")
            else:
                 print(f"\nVocê acertou o número: {numero_aleatorio_escolhido}\nTentativas Restantes: {chances}.\n")
                 break
            if chances == 0:
                print(f"Você perdeu! Número escolhido pela máquina: {numero_aleatorio_escolhido}")
            
gerar_numero_aleatorio()