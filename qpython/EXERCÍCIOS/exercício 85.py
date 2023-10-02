núm = [[], []]
n = 0
for c in range (1,8):
     n = int(input(f'Digite o {c}º valor: '))
     if n % 2 == 0:
         núm[0].append(n)          
     elif n % 2 == 1:
         núm[1].append(n)
print('-='*21)
núm[0].sort()
núm[0].sort()
print (f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')