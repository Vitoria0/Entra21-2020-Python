#Calcule o valor total dos itens e aplique descontos
#Se o valor for superior a 50, 2% de desconto
#Se o valor for superior a 100, 5% de desconto
#Se o valor for superior a 200, 10% de desconto
#Descyubra qual o item mais caro da lista
#Ordene os itens da lista por ordem alfabetica

itens = {'Anel':50, 'Bracelete':170, 'Brincos':90, 'colar':250, 'Coroa':500, 'Pulseira':25, 'Tiara':250}
tot = itens.values()
if X > 50:
    p1 = (X * 2 / 100)
    p2 = X - p1
elif X > 50 and > 100:
    p1 = (X * 5 / 100)
    p2 = X - p1
elif X > 50 and > 100 and > 200:
    p1 = (X * 10 / 100)
    p2 = X - p1
soma = sum(tot)
print('A soma de todos os itens é {}'.format(soma))