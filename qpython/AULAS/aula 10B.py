n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
m = (n1+n2)/2
print ('A média é igual a {:.1f}'.format(m))
'''if m >=6.0:
   print ('Sua nota foi boa! Parabéns!')
else:
   print ('Sua média foi ruim! Estude mais')'''

print('PARABÉNS!' if m >=6 else 'Estude Mais!')
