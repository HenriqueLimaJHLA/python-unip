def media_notas():
    notas = []
    media = 0
    for i in range(4):
        i += 1
        nota = float(input(f"Digite a nota {i}: "))        
        notas.insert(i, nota)
        media = notas        

    media = (sum(media)) / len(media)
    print(f"A média dos núumeros é de {media}")
    
media_notas()