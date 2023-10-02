times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MN', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*10)
print(f'Lista de times do Brasileirão : {times}')
print('-='*10)
print(f'Os cinco primeiros são:{times[0:5]}')
print('-='*10)
print(f'Os quatro últimos são: {times[16:20]}')
print('-='*10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*10)
posição = times.index('Chapecoense') +1
print(f'O Chapecoense está na {posição}ª posição')
    

