from os import system, name 

palavra = ' '
chances = 0

def jogar():
    palavra = "abelha"
    chances = 5
    letras_usadas = [ ]
    while True:
        tentativa_palavra = ' '

        # for windows 
        if name == 'nt': 
            system('cls')

        # for mac and linux(here, os.name is 'posix') 
        else: 
            system('clear')       
  
        print("Número de chances: %d - tentativas:" % chances) # interpolação de string
        print(*letras_usadas) # imprime item por item do array
        print("\n")
        for x in palavra:
            tentativa_palavra += x if x in letras_usadas else "_"
        print(tentativa_palavra + "\n\n")
       
        chute = input("Digite uma letra:")
        letras_usadas.append(chute)
        
        if not chute in palavra:
            chances -= 1
        
        if chances == 0:
            print("Você perdeu!")
            break
        if tentativa_palavra == palavra:
            print(f'Você ganhou com apenas {chances}')
            break

with open('arquivo1.txt', 'r') as f:
    for line in f:
        print(line.read())

if __name__ == "__main__":
    #jogar()
    pass