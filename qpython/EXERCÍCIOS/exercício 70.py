print('_ '*21)
nome = 'LOJA SUPER BARATÃO'
print(f'{nome:^38}')
print('_ '*21)
soma = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))  
    preço = float(input('Preço: R$ '))
    cont += 1
    soma += preço
    if preço > 1000:        
       totmil += 1
    if cont == 1:
       menor = preço
       barato = produto
    else:
       if preço < menor:
           menor = preço
           barato = produto   
    resp = ' '
    while resp not in 'SN':
      resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
       break
print('FIM DO PROGRAMA')
print (f'O Total da compra foi R${soma:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
