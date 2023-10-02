from random import randint
from time import sleep
print('--'*21)
print('JOGO DA MEGASENA')
print ('--'*21)
n = int(input('Quantos jogos você quer que eu sorteie?' ))
print(f'SORTEANDO {n} JOGOS')
for c in range (1,n+1):
    sleep(1.2)
    núm = [randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(0,60)]
    núm.sort()
    print(f'Jogo {c} : {núm}')
print('< BOA SORTE! >')

   
      
      
      