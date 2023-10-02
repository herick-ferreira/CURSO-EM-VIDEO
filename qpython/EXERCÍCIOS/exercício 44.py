print('{:=^40}'.format(' LOJAS GUANABARA '))
compras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print ('[1] à vista dinheiro/cheque \n[2] à vista cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão')
opc = int(input('Qual a opção?  '))
if opc == 1:
    juros = compras - (compras*0.1)  
elif opc == 2:
    juros = compras - (compras*0.05)
elif opc == 3:
     parcela = compras/2
     juros = compras * 1
     print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opc == 4:
    parcelas = int(input ('Quantas parcelas? '))
    juros = compras + (compras*0.2)
    parcelona = juros/parcelas
    print ('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, parcelona))
else:
    juros = compras
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compras, juros)) 