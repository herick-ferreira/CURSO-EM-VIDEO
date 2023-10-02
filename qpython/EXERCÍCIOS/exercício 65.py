quant = media = maior = menor = 0
tot = 0
soma = 0
opc = 'S'
while opc in 'Ss':        
   n = int(input('Digite um número: '))
   opc = str(input('Quer continuar? [S/N]  ')).upper().strip()[0] 
   soma += n
   quant += 1
   if quant == 1:
     maior = menor = n
   else:
     if n > maior:
       maior = n
     if n < menor:
       menor = n
media += soma/quant
print('Você digitou {} números e a média foi {:.2f}\nO maior valor foi {} e o menor foi {}.'.format(quant, media,maior,menor))
      