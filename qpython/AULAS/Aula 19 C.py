pessoas = {'nome': 'Gustavo', 'sexo' : 'M', 'idade': 22}
for k in pessoas.keys():
      print(k)
print()

for k in pessoas.values():
      print(k)
print()
      
for k, v in pessoas.items():
      print(f'{k} = {v}')
print()
      
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
      print(f'{k} = {v}')
print()

pessoas ['peso'] = 98.5
for k, v in pessoas.items():
      print(f'{k} = {v}')
print ()
      
del pessoas ['sexo']
for k, v in pessoas.items():
      print(f'{k} = {v}')
print()


