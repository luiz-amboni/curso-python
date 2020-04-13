import random

def ordvet1():
    lista1 = []
    n = int(1)
    troca1 = int(1)
    qtdcomparacoes1 = int(0)
    qtdtrocas1 = int(0)
    resultados1 = []

    for i in range(0, 10):
        lista1.append(random.randint(1, 100))

    while n <= len(lista1) and troca1 == 1:
        troca1 = 0
        for i in range(0, (len(lista1)-1)):
            qtdcomparacoes1 += 1
            if lista1[i] < lista1[i + 1]:
                troca1 = 1
                aux = lista1[i]
                lista1[i] = lista1[i + 1]
                lista1[i + 1] = aux
                qtdtrocas1 += 1
        n += 1
    print(lista1)
    resultados1.append(qtdcomparacoes1)
    resultados1.append(qtdtrocas1)
    return resultados1

ordvet1()