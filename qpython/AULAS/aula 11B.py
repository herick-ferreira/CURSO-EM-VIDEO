nome = 'Guanabara'
'''print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))'''
cores = {'limpa' :'\033[m',
               'azul' : '\034[m',
               'amarelo': '\033[33m',
               'preto e branco' : '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['preto e branco'], nome, cores['limpa']))