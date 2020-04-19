import sortstring
import sortstringmelhorado
import sortstringmelhorado2

def menustring():
    menuseletor = int(input('Escolha a opção que deseja >>\n[1] Sort\n[2] Sort 1° versão melhorado\n[3] Sort 2° versão melhorado\n'))

    if menuseletor == 1:
        sortstring.ordsortstring()
    elif menuseletor == 2:
        sortstringmelhorado.ordsortstringmelhorado()
    elif menuseletor == 3:
        sortstringmelhorado2.ordsortstringmelhorado2()
    else:
        print('[ERRO!!!] Por favor digite um valor válido!')

