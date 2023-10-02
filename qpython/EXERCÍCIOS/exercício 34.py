salário = float(input('Qual é o salário do funcionário?R$'))
if salário >= 1250.00:
    reajuste = (salário/10)+salário 
else:
    reajuste = (salário/100)*15+salário
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário,reajuste))