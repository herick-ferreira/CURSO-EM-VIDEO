def notas(*n, sit=False):
       """
       =>doc
       """
       
       r = dict()
       r['total'] = len(n)
       r['maior'] = max(n)
       r['menor'] = min(n)
       r['média'] = sum(n)/len(n)
       if sit:
           if r['média'] >= 7:
               r['Situação'] = 'BOA!'
           elif r['média'] >= 5:
               r['Situação'] = 'RAZOÁVEL!'
           else:
               r['Situação'] = 'RUIM!'
       return r
      
       
resp = notas(2,8,9,8,sit =True)
print(resp)   

help(notas)