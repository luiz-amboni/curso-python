import menuint
import menuchar
import menustring

menuSeletor = int(input('Escolha a opção que desejar: \n[1]Ordenação de inteiros\n[2]Ordenação de caracteres\n[3]Ordenação de Strings\n'))

if menuSeletor == 1:
    menuint.menuint()
elif menuSeletor == 2:
    menuchar.menuchar()
elif menuSeletor == 3:
    menustring.menustring()
else:
    print('[ERRO!!!] Por favor digite um valor válido!')
