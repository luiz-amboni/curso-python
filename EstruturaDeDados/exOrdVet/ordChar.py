#Ordenar vetores com characteres.
import random
import string


def ordchar(menuCresDesc):
    lista = []

    for c in range(0, 13):
        lista.append(random.choice(string.ascii_lowercase))

    for c in range(0, len(lista)):
        for c2 in range(0, len(lista)):
            if ord(lista[c]) < ord(lista[c2]):
                aux = lista[c]
                lista[c] = lista[c2]
                lista[c2] = aux

    if menuCresDesc == 2:
        lista.reverse()

    for c in range(0, len(lista)):
        print(f'{lista[c]}')
