from time import sleep

def frase (msg):
     print('_'*41)
     print(msg.center(41))
     print('_'*41)


while True:
     frase('MENU PRINCIPAL')
     print('1- Ver pessoas cadastradas\n2- Cadastrar Nova Pessoa\n3- Sair do sistema')
     try:
         opc = int(input('Sua opção: '))
     except(ValueError, TypeError):
         sleep(1.5)
         print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
     else:
         if opc not in (1,2,3):
            sleep(1.5)
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
         elif opc == 1:
            frase('Opção 1')
         elif opc == 2:
            frase('Opção 2')
         else:
             frase('Saindo do sistema...Até logo!')                
             sleep(1.5)
             break


     