import random

def ordsortintmelhorado2():
    lista1 = []
    lista2 = []
    n = int(1)
    troca = int(1)

    for i in range(0, 3000):
        lista1.append(random.randint(1, 100))

    for i in range(0, 5000):
        lista2.append(random.randint(1, 100))

    while n <= len(lista1) and troca == 1:
        troca = 0
        for i in range(0, (len(lista1)-1)):
            if lista1[i] < lista1[i + 1]:
                troca = 1
                aux = lista1[i]
                lista1[i] = lista1[i + 1]
                lista1[i + 1] = aux
        n += 1

    while n <= len(lista2) and troca == 1:
        troca = 0
        for i in range(0, (len(lista2)-1)):
            if lista2[i] < lista2[i + 1]:
                troca = 1
                aux = lista2[i]
                lista2[i] = lista2[i + 1]
                lista2[i + 1] = aux
        n += 1

