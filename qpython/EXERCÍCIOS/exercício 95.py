jogador = dict()
partidas = list()
grupo = list()
while True:    
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range (0,tot):
         partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    grupo.append(jogador.copy())    
    while True:
         resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]             
         if resp in 'SN':
            break
         print('ERRO! Por favor, digite apenas S ou N.')         
    if resp == 'N':
         break
print('-='*21) 
print('cod', end = ' ')
for i in jogador.keys():
    print (f'{i:<15}', end =' ')
print()
print('-='*21) 
for k,v in enumerate(grupo):
    print(f'{k:>3}', end =' ')
    for d in v.values():
        print(f'{str(d):<15}', end =' ')
    print()
print('-='*21)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar) '))
    if busca == 999:
        break
    if busca >= len(grupo):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'     ---- LEVANTAMENTO DO JOGADOR {grupo[busca]["nome"]}: ')
        for i, g in enumerate(grupo[busca]['gols']):
              print(f'      No jogo {i+1} fez {g} gols.')
    print('=-'*21)
print('               << VOLTE SEMPRE >>            ')