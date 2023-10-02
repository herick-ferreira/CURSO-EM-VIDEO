números = []
while True:
     n = int(input('Digite um valor: ')) 
     if n not in números:
         números.append(n)
         print('Valor adicionado com sucesso...')
     else:
         print('Valor dupicado! Não vou adicionar...')
     resp = ' '
     while resp not in 'SN':
       resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
     if resp == 'N':
       break 
print('-='*21)
números.sort()
print(f'Você digitou os valores {números} ')
