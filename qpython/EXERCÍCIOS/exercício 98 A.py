from time import sleep
def contador(ínicio, fim, passo):
    print ('-='*21)
    
    for c in range (ínicio, fim+1, passo):
        print(f'{c}', end = ' ', flush=True)
        sleep(0.15)
    print('FIM')
        
        
        
        
print('Contagem de 1 até 10 de 1 em 1')
contador(1,10,1)

print('\nContagem de 10 até 0 de 2 em 2')
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input ('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

print(f'Contagem de {i} até {f} em {p}')
contador(i,f,p)
if i < 0:
    i *= -1
if f < 0:
    f *= -1  
if p < 0:
    p *= -1
if i == 0:
    i = 1
if f == 0:
    f = 1  
if p == 0:
    p = 1    
 


