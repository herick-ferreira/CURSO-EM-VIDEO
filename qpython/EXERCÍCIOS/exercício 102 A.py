def fatorial (num, show=0):      
      print('_'*42)
      if show == True:
         for c in range (num,-1+1,-1):
              print('{}'.format(c), end ='')
              print(' x ' if c > 1 else ' = ' , end='')
         f=1
         for c in range (num,0,-1):
             f *= c
         return f
      else:
         f = 1
         for c in range (num,0,-1):
            f *= c
         return f
       

print(fatorial(1,True))