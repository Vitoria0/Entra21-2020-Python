import random
from time import sleep
titulo = '\033[35mJOGO DA FORCA'
undeline1 = ['_', '_', '_', '_', '_', '_']
undeline2 = ['_', '_', '_', '_', '_', '_', '_',]
undeline3 = ['_', '_', '_', '_', '_', '_',]
undeline4 = ['_', '_', '_', '_', '_', '_', '_', '_']
undeline5 = ['_', '_', '_', '_', '_', '_', ]
palavras = ('ABELHA', 'LAGARTO', 'CAVALO', 'CACHORRO', 'RAPOSA')
palavra_secreta = random.choice(palavras)
letras_usadas = [ ]
tentativas = 10
acertos = 0

print('\033[35m~' * 50)
print(f'{titulo:^50}')
print('\033[35m~' * 50)
print('\n')

game = str(input('Deseja jogar? ')).strip().upper()[0]

if game == 'S':
    print('Você tem 10 chances para acertar a palavra')
    print('\033[35mPensando em uma palavra...')
    sleep(1)
    print(f'\033[35mA palavra escolhida tem {len(palavra_secreta)} letras')
    print('_' * len(palavra_secreta))

else:
    print('\033[1;4;31mOk! Volte quando quiser jogar')

while True:
    letra = str(input('\033[35mEscolha uma letra: ')).strip().upper()
    letras_usadas.append(letra)
    print(f'Letras entadas {letras_usadas}')

    if palavra_secreta == 'ABELHA':
        if letra in palavra_secreta:
            print(f'Você acertou uma letra na {palavra_secreta.index(letra)}')
            undeline1[palavra_secreta.index(letra)] = letra
            print(undeline1)
            acertos += 1
        else:
            print('Tente novamente')
            tentativas -= 1
            print(f'Agora você tem {tentativas}')
            if tentativas <= 0:
                print('\nGAME OVER')
                break
            if acertos == 6:
                print('Você ganhou!')
                print(f'A palavra escolhida foi {palavra_secreta}')
                break

    elif palavra_secreta == 'LAGARTO':
        if letra in palavra_secreta:
            print('Você acertou uma letra na {palavra_secreta.index(letra)}')
            undeline2[palavra_secreta.index(letra)] = letra
            print(undeline2)
            acertos += 1
        else:
            print('Tente novamente')
            tentativas -= 1
            print(f'Agora você tem {tentativas}')
            if tentativas <= 0:
                print('\nGAME OVER')
                break
            if acertos == 7:
                print('Você ganhou!')
                print(f'A palavra escolhida foi {palavra_secreta}')
                break

    elif palavra_secreta == 'CAVALO':
        if letra in palavra_secreta:
            print('Você acertou uma letra na {palavra_secreta.index(letra)}')
            undeline3[palavra_secreta.index(letra)] = letra
            print(undeline3)
            acertos += 1
        else:
            print('Tente novamente')
            tentativas -= 1
            print(f'Agora você tem {tentativas}')
            if tentativas <= 0:
                print('\nGAME OVER')
                break
            if acertos == 6:
                print('Você ganhou!')
                print(f'A palavra escolhida foi {palavra_secreta}')
                break

    elif palavra_secreta == 'CACHORRO':
        if letra in palavra_secreta:
            print('Você acertou uma letra na {palavra_secreta.index(letra)}')
            undeline4[palavra_secreta.index(letra)] = letra
            print(undeline4)
            acertos += 1
        else:
            print('Tente novamente')
            tentativas -= 1
            print(f'Agora você tem {tentativas}')
            if tentativas <= 0:
                print('\nGAME OVER')
                break
            if acertos == 8:
                print('Você ganhou!')
                print(f'A palavra escolhida foi {palavra_secreta}')
                break

    elif palavra_secreta == 'RAPOSA':
        if letra in palavra_secreta:
            print('Você acertou uma letra na {palavra_secreta.index(letra)}')
            undeline5[palavra_secreta.index(letra)] = letra
            print(undeline5)
            acertos += 1
        else:
            print('Tente novamente')
            tentativas -= 1
            print(f'Agora você tem {tentativas}')
            if tentativas <= 0:
                print('\nGAME OVER')
                break
            if acertos == 6:
                print('Você ganhou!')
                print(f'A palavra escolhida foi {palavra_secreta}')
                break

print('Até a próxima!')