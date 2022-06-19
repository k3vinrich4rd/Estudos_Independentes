secreto = 'perfume'  # palavra da forca
digitadas = []  # lista vazia
chances = 3  # Números de chances que o usuário tem

while True:  # While = Enquanto
    if chances <= 0:  # if = Se
        print('Você perdeu abestado 😅🤡,  tente novamente!!!')
        break  # Break = Termina o laço

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale 😔😖💔, digite apenas uma letra!!! ')
        continue

    digitadas.append(letra)  # # Insere um novo valor no final da lista

    if letra in secreto:
        print(f'AEEEEEEE🎉🎊, a letra "{letra}" esxiste na palavra secreta.')
    else:
        print(f'AAaaaaaa😭, a letra "{letra}" não existe na palavra secreta.')
        digitadas.pop()  # deleta o último elemento de uma lista

    secreto_temporario = ''  # Onde as letras corretas vão ser armazenads
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta  # secreto_temporario = secreto_temporario + letra_secreta
        else:  # Se não
            secreto_temporario += '_'  # Espaço para preencher as letras

    if secreto_temporario == secreto:
        print(f'PARABÉNS, VOCÊ GANHOU💖!!!  A palavra secreta era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta era "{secreto_temporario}" ')

    if letra not in secreto:
        chances -= 1  # chances = chances - 1

    print(f'Você ainda tem {chances} chances🐍🐍🐍.')
    print()
