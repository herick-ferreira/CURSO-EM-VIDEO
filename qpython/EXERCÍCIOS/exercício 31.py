d = int(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {}km.'.format(d))
preço = d * 0.5 if d <= 200 else d * 0.45
'''if d <= 200:
    preço = d*0.50
else:
    preço = d*0.45'''
print('E o preço de sua passagem será de R${:.2f}'.format(preço))