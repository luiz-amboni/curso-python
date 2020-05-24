import sortint
import sortintmelhorado
import sortintmelhorado2
import sortchar
import sortcharmelhorado
import sortcharmelhorado2

menuSeletor = int(input('Escolha a opção que desejar: \n[1]Ordenação de inteiros;\n[2]Ordenação de caracteres;\n[3]Ordenação de Strings.\n'))

if menuSeletor == 1:
    resultadosortint = sortint.ordsortint()
    resultadosorintmelhorado = sortintmelhorado.ordsortintmelhorado()
    resultadosorintmelhorado2 = sortintmelhorado2.ordsortintmelhorado2()
    print(f'Diferença de comparações vetor de 3000 - 5000: ')
    print(f'\nSort {resultadosortint[0]}  Sort1° {resultadosorintmelhorado[0]}  Sort2° {resultadosorintmelhorado2[0]}')
    print(f'Diferença de trocas vetor de 3000 - 5000: ')
    print(f'\nSort {resultadosortint[1]}  Sort2° {resultadosorintmelhorado[1]}  Sort2° {resultadosorintmelhorado2[1]}')
    print(f'Diferença de tempos vetor de 3000 - 5000: ')
    print(f'\nSort {resultadosortint[2]}  Sort2° {resultadosorintmelhorado[2]}  Sort2° {resultadosorintmelhorado2[2]}')
elif menuSeletor == 2:
    print()
