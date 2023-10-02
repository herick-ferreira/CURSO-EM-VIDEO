from time import sleep
n = int(input('Primeiro Valor: '))
m = int(input('Segundo Valor: '))
opc = 0
while opc != 5:
     print('⚫'*30)
     print('''           [1] somar
           [2] multiplcar
           [3] maior
           [4] novos números
           [5] sair do programa''')     
     print('⚫'*30)
     opc = int(input ('>>>>Qual é a sua opção? '))         
     if opc == 1:
        print('A soma entre {} + {} é {}'.format(n, m, n+m))
     elif opc == 2:
        print('O resultado de {} X {} é {}'.format(n, m, n*m))
     elif opc == 3:
        if n > m:
           print('Entre {} e {} o maior valor é {}'.format(n, m, n))
        else:
          	print('Entre {} e {} o maior valor é {}'.format(n, m, m))
     elif opc == 4:
        print('Informe novos números:') 
        n = int(input('Primeiro Valor: '))
        m = int(input('Segundo Valor: '))
     elif opc == 5:
        print('Finalizando...')         
     else: 
        print('Opção Inválida. Tente novamente')
     print('=-=='*10)
     sleep(2) 
print('Fim do programa! Volte Sempre!')              
              
     
      

                
                
          