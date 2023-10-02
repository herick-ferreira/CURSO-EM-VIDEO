from random import randint
computador = randint (0,10)
palpite = 0
cont = 0
print ('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while palpite != computador:              
       palpite = int(input('Qual é o seu palpite? '))         
       if palpite > computador:
          print('Menos... tente mais uma vez.')
       if palpite < computador:
          print('Mais... tente mais uma vez.')
       cont += 1
print('Acertou com {} tentativas. Parabéns!'.format(cont))     