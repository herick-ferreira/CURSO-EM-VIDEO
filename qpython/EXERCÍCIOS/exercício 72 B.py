cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    número = int(input('Digite um número entre 0 e 20: '))  
    if 0<= número < 20:
       print(f'Você digitou o número {cont[número]}')
    else:
       print('Tente novamente.', end =' ')
    resp = ' '
    while resp not in 'SN':
      resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
      break   
      
      
      
