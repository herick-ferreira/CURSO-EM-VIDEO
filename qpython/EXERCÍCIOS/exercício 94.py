dados = dict()
grupo = list()
soma = media = 0
while True:
     dados.clear()
     dados['nome'] = str(input('Nome: '))
     while True:
         dados['sexo'] = str(input('Sexo: ')).strip().upper()[0]
         if dados['sexo'] in 'MF':
             break
         print('ERRO! Por favor, digite apenas M ou F.')         
     dados['idade'] = int(input('Idade: '))
     soma += dados['idade'] 
     grupo.append(dados.copy())
     while True:
         resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]             
         if resp in 'SN':
            break
         print('ERRO! Por favor, digite apenas S ou N.')         
     if resp == 'N':
         break
print('-='*21)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
media = soma/len(grupo)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end = ' ')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end =' ')
    else:
        print('Não há!')
print()
print(f'D) Lista de pessoas que estão acima da média: ', end = ' ')
for p in grupo:
    if p['idade'] >= media:
        print('    ')
        for k,v in p.items():
            print(f'{k} = {v}; ', end = ' ')
        print()
print('            << ENCERRADO >>>           ')

     