from datetime import datetime
dados = dict()
tudo = dict() 
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira'] = int(input('CTPS (0 não tem): '))
if dados['carteira'] != 0:
    dados ['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados ['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*21)
for k, v in dados.items():
    print(f'   -- {k} tem valor {v}')

