#Arquivo principal / Menu.
import ordInt02
import ordChar
import ordString
import sys


menuOrdens = int(input('Escolha a opção que desejar: \n [1]Ordenar Números \n [2] Ordenar characteres \n [3] Ordenar Nomes \n'))
menuCresDesc = int(input('Escolha a opção que desejar: \n [1] Crescente \n [2] Decrescente \n'))

if menuCresDesc != 1 and menuCresDesc != 2:
    print('[ERRO] Digite um valor válido para o tipo de ordenação!!!')
    sys.exit()

if menuOrdens == 1:
    ordInt02.ordenaNumero(menuCresDesc)
elif menuOrdens == 2:
    ordChar.ordchar(menuCresDesc)
elif menuOrdens == 3:
    ordString.ordstring(menuCresDesc)
else:
    print('[ERRO] Digite um valor válido para o tipo de dado!!!')
    sys.exit()
