#Crie uma lista com todas as letras do alfabeto
#REmova as vogais dessa lista e crie uma tupla com elas

alf = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h','i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x','y', 'z']
vogal = ('a', 'e', 'i', 'o', 'u')
alf.remove('a')
alf.remove('e')
alf.remove('i')
alf.remove('o')
alf.remove('u')
print(alf)
print(vogal)

nome = ['N', 'I', 'C', 'K']
nome2 = ('N', 'I', 'C', 'K')
nome.remove('I')
nome.append('16')
nome.append('Um Momento de Silencio')
print(nome)
print(nome2)
