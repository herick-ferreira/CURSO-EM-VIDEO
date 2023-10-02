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

