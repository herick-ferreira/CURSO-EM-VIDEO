def metade (preço=0):
    res = preço/2
    return res 

def dobro (preço=0):
    res = preço*2
    return res 


def aumentar (preço=0,n=0):
    res = preço + (preço*n/100)
    return res 

    
def diminuir (preço=0,n=0):
    res = preço - preço*0.01* n 
    return res

    