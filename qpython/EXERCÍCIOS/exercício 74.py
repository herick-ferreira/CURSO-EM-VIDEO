from random import randint
números = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end =' ')
for n in números:
    print(f'{n}', end =' ')
print(f'\nO maior valor sortedo foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')   
    
