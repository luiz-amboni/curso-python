import sortint
import sortintmelhorado
import sortintmelhorado2
import sortchar
import sortcharmelhorado
import sortcharmelhorado2

menuSeletor = int(input('Escolha a opção que desejar: \n[1]Ordenação de inteiros;\n[2]Ordenação de caracteres;\n[3]Ordenação de Strings.\n'))

if menuSeletor == 1:
    sortint.ordsortint()
    resultadosorintmelhorado = sortintmelhorado.ordsortintmelhorado()
    sortintmelhorado2.ordsortintmelhorado2()
