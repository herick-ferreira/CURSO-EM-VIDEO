def voto (ano):
     from datetime import date
     n = date.today().year
     idade = n - ano
     if idade < 16:
         return f'Com {idade} anos:  NÃO VOTA'
     elif 16 <= idade < 18:
         return f'Com {idade} anos o VOTO É OPCIONAL'
     elif 18 <= idade < 65:
         return f'Com {idade} anos: VOTO OBRIGATÓRIO'
     elif idade >= 65:
         return f'Com {idade} anos: o VOTO É OPCICIONAL'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

     

     
