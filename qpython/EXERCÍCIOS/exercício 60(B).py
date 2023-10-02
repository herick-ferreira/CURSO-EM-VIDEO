from math import factorial
n = int(input('Digite  número para calcular seu fatorial: '))
f = factorial(n)
print('Calculando o fatorial de {}! = '.format(n), end='')
for c in range (n,-1+1,-1):
    print( '{}'.format(c), end ='')
    print(' x ' if c > 1 else ' = ' , end='')
print('{}'.format(f))
    