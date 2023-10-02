num = list()
par = list()
ímpar = list()
while True:
     num.append(int(input('Digite um valor: ')))
     resp = ' '
     while resp not in 'SN':
       resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
     if resp == 'N':
       break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        ímpar.append(v)
print('-='*21)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {ímpar}')
