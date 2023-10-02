salário = float(input('Qual é o salário do funcionário?R$'))
print ('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, (salário + salário*0.15)))