cont = 0
soma = 0
n = 0
while n != 999:    
      n = int(input('Digite um numero [999 para parar]: '))
      cont += 1
      soma += n
print('Você digitou {} números e a soma entre eles foi {}'.format((cont-1), (soma-999)))