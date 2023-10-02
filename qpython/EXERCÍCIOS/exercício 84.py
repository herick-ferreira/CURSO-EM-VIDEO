dado = list()
galera = list()
maior = menor = 0
cont = 1
while True:
     dado.append(str(input('Nome: ')))
     dado.append(float(input('Peso: ')))
     if len(galera) == 0:
         maior = menor = dado[1]
     else:
         if dado[1] > maior:
            maior = dado[1]
         if dado[1] < menor:
            menor = dado[1]
     galera.append(dado[:])
     dado.clear()
     resp = ' '
     while resp not in 'SN':
       resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
     if resp == 'N':
       break
     cont+= 1
print('-='*21)
print(f'Ao todo você cadastrou {cont} pessoas. ')
print(f'O maior peso foi {maior}Kg. Peso de ', end = ' ')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}', end =' ')
print()
print(f'O menor peso foi {menor}Kg. Peso de ' ,end ='  ')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}', end = ' ')
print()

         
