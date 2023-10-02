from random import randint
from time import sleep
computador = randint(0, 5)
#print('Pensei no número {}'.format(computador))
print ('-=-' *14)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print ('-=-' *14)
jogador = int(input ('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(4)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
