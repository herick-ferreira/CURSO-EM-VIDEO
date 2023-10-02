print('Gerador de PA')
print('-='*21)
p = int(input ('Primeiro termo: '))
r = int(input ('Razão da P.A: '))
termo = p
cont = 1
while cont <= 10:
    print('{}'.format(termo), end = ' → ')
    termo += r
    cont += 1
print('FIM')
