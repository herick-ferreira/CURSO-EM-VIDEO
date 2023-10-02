from random import randint
print('=-'*21)
print('Vamos Jogar par ou ímpar')
print('=-'*21)
v = 0
while True:   
    jogador = int(input ('Diga um valor: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*21)
    print (f'Você jogou {jogador} e o computador {computador}. Total de {total}', end = '') 
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print ('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')

       

  

    