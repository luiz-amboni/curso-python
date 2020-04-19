import sortchar
import sortcharmelhorado
import sortcharmelhorado2

def menuchar():
    menuseletor = print(int(input('Escolha a opção que deseja >>\n[1] Sort\n[2] Sort 1° versão melhorado\n[3] Sort 2° versão melhorado\n')))

    if menuseletor == 1:
        sortchar.ordsortchar()
    elif menuseletor == 2:
        sortcharmelhorado.ordsortcharmelhorado()
    elif menuseletor == 3:
        sortcharmelhorado2.ordsortcharmelhorado2()
    else:
        print('[ERRO!!!] Por favor digite um valor válido!')
