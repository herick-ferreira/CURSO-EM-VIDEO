d = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
valor = (km*0.15) + (60*d)
print ('O total a pagar é de R${:.2f}'.format(valor))