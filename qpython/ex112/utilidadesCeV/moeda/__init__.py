def metade (preço=0, formato=False):
    res = preço/2
    return res if formato is False else moeda(res)

def dobro (preço=0,formato=False):
    res = preço*2
    return res if formato is False else moeda(res)


def aumentar (preço=0,n=0,formato=False):
    res = preço + (preço*n/100)
    return res if formato is False else moeda(res)

    
def diminuir (preço=0,n=0,formato=False):
    res = preço - preço*0.01* n 
    return res if formato is False else moeda(res)

     
def moeda (preço=0,moeda = 'R$'):
      return f'{moeda}{preço:>2.2f}'.replace('.',',')
"""
def resumo (preço=0, aumento=0, redução=0):
      print('_'*32)
      print(f'{"RESUMO DO VALOR":^32}')
      print('_'*32)
      print(f'Preço analisado:' {"R$":>9}{preço:>3.2f}'.replace('.',','))
      print(f'Dobro do preço:' {"R$":>10}{preço*2:>5.2f}'.replace('.',','))
      print(f'Metade do preço:' {"R$":>10}{preço/2:5.2f}'.replace('.',','))
      print (f'{aumento}% de aumento:' {"R$":>10}{preço+(aumento/100*preço):5.2f}'.replace('.',','))
      print(f'{redução}% de redução:' {"R$":>10}{preço-preço*0.01*redução:5.2f}'.replace('.',','))
      print('_'*32)
"""
def resumo(preço=0, taxaa= 10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço,taxaa,True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço,taxar,True)}')
