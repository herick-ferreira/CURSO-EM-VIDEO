#from math import factorial
n = int(input('Digite  número para calcular seu fatorial: '))
#f = factorial (n)
c = n
f = 1
print('Calculando o fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ' , end='')
    f *= c
    c -= 1
print('{}'.format(f))
