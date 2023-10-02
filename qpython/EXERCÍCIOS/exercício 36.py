vc = float(input('Valor da casa:R$'))
salário = float(input('Sálario do comprador: R$'))
fin = int(input('Quantos anos de financiamento?'))
prestação = vc/(fin*12)
print('Para pegar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(vc, fin, prestação))
if prestação > salário*0.3:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')

