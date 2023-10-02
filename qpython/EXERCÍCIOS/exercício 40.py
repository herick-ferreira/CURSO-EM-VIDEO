p = float(input('Primeira nota:'))
s = float(input('Segunda nota:'))
média = (p + s)/2
print ('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(p,s, média))

if 7> média >=5:
   print ('O aluno está de RECUPERAÇÃO.')
elif média < 5.0:
   print ('O aluno está REPROVADO.')
elif média >= 7:
   print ('O aluno está APROVADO.')