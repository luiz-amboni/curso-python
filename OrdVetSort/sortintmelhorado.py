import random

def ordsortintmelhorado():
    lista1 = []
    lista2 = []

    for i in range(0, 3000):
        lista1.append(random.randint(1, 100))

    for i in range(0, 5000):
        lista2.append(random.randint(1, 100))

    for i in range(0, (len(lista1)-1)):
        for i2 in range((len(lista1)-1), i, -1):
            if lista1[i2] < lista1[i2 - 1]:
                aux = lista1[i2]
                lista1[i2] = lista1[i2-1]
                lista1[i2 - 1] = aux

    for i in range(0, (len(lista2)-1)):
        for i2 in range((len(lista2)-1), i, -1):
            if lista2[i2] < lista2[i2 - 1]:
                aux = lista2[i2]
                lista2[i2] = lista2[i2-1]
                lista2[i2 - 1] = aux

