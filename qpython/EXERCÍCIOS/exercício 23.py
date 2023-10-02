número = int(input('Informe um número:'))
#n = str(número)
'''print ('Analisando o número {}'.format(número))
print ('Unidade: {}'.format (n [3]))
print ('Dezena: {}'.format (n [2]))
print ('Centena: {}'.format (n [1]))
print ('Milhar: {}'.format (n [0]))'''

u = número //1 % 10
d = número //10 % 10
c = número //100 % 10
m = número //1000 % 10

print ('Analisando o número {}'.format(número))
print ('Unidade: {}'.format (u))
print ('Dezena: {}'.format (d))
print ('Centena: {}'.format (c))
print ('Milhar: {}'.format (m))

