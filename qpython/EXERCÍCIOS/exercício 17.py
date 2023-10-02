'''op = float(input ('Comprimento do cateto oposto:'))
ad = float(input('Comprimento do cateto adjacente:'))
hip1 = (op*op) + (ad*ad)
hip2 = hip1**0.5
print ('A hipotenusa vai medir {:.2f}'.format(hip2))'''

import math
op = float(input ('Comprimento do cateto oposto:'))
ad = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(op, ad)
print ('A hipotenusa vai medir {:.2f}'.format(hi))
