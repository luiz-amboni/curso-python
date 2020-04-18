import random
import time

def ordsortintmelhorado2():

    def ordvet1():
        lista1 = []
        n = int(1)
        troca1 = int(1)
        qtdcomparacoes1 = int(0)
        qtdtrocas1 = int(0)
        resultados1 = []

        for i in range(0, 3000):
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
        resultados1.append(qtdcomparacoes1)
        resultados1.append(qtdtrocas1)
        return resultados1

    def ordvet2():
        lista2 = []
        n = int(1)
        troca2 = int(1)
        qtdcomparacoes2 = int(0)
        qtdtrocas2 = int(0)
        resultados2 = []

        for i in range(0, 5000):
            lista2.append(random.randint(1, 100))

        while n <= len(lista2) and troca2 == 1:
            troca2 = 0
            for i in range(0, (len(lista2)-1)):
                qtdcomparacoes2 += 1
                if lista2[i] < lista2[i + 1]:
                    troca2 = 1
                    aux = lista2[i]
                    lista2[i] = lista2[i + 1]
                    lista2[i + 1] = aux
                    qtdtrocas2 += 1
            n += 1
        resultados2.append(qtdcomparacoes2)
        resultados2.append(qtdtrocas2)
        return resultados2

    inicio1 = time.time()
    resultados1 = ordvet1()
    fim1 = time.time()

    inicio2 = time.time()
    resultados2 = ordvet2()
    fim2 = time.time()

    difcomparacoes = resultados2[0] - resultados1[0]
    diftroca = resultados2[1] - resultados1[1]
    tempovet1 = fim1 - inicio1
    tempovet2 = fim2 - inicio2
    diftempo = tempovet2 - tempovet1

