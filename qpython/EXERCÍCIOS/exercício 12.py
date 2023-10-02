produto = float(input('Qual é o preço do produto?R$'))
print ('O produto que custava {}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto, (produto - produto*0.05)))