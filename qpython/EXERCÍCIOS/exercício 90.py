dado = dict()
dado['Nome'] = str(input ('Nome: '))
dado['Media'] = float(input(f'Média de {dado["Nome"]}: '))
if dado['Media'] >= 7 :
    dado['Situação'] = 'Aprovado'
elif 5<= dado['Media'] < 7:
    dado['Situação'] = 'Recuperação'
else:
    dado['Situação'] = 'Reprovado'
for k,v in dado.items():
    print(f'{k} é igual a {v}')

