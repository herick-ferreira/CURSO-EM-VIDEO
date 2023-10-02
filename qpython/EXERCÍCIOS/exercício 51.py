print ('='*42)
print('{:^40}'.format(' 10 TERMOS DE UMA PA '))
print ('='*42)
p = int (input('Primeiro Termo: '))
r = int (input ('Razão: '))
décimo = p + (10-1) * r
for c in range (p, décimo + r,r):
    print('{}'.format(c), end = '→ ')
print('ACABOU')
      