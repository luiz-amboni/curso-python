import sortint
import sortintmelhorado
import sortintmelhorado2

def menuint():
    menu = (int(input('Escolha a opção que deseja >>\n[1] Sort\n[2] Sort 1° versão melhorado\n[3] Sort 2° versão melhorado\n')))

    if menu == 1:
        sortint.ordsortint()
    elif menu == 2:
        sortintmelhorado.ordsortintmelhorado()
    elif menu == 3:
        sortintmelhorado.ordsortintmelhorado()
    else:
        print('[ERRO!!!] Por favor digite um valor válido!')

