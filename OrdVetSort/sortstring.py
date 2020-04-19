import random
import time
import string


def ordsortstring():

    def ordvet1():

        lista1 = []
        qtdcomparacoes1 = int(0)
        qtdtrocas1 = int(0)
        resultados1 = []

        for i in range(0, 30):
            slista = ""
            for i2 in range(0, 20):
                slista = slista + random.choice(string.ascii_letters)
            lista1.append(slista)

        for i in range(0, len(lista1)):
            for i2 in range(0, (len(lista1) - 1)):
                qtdcomparacoes1 += 1
                if lista1[i2] > lista1[i2 + 1]:
                    aux = lista1[i2]
                    lista1[i2] = lista1[i2 + 1]
                    lista1[i2 + 1] = aux
                    qtdtrocas1 += 1
        resultados1.append(qtdcomparacoes1)
        resultados1.append(qtdtrocas1)
        return resultados1

    def ordvet2():

        lista2 = []
        qtdcomparacoes2 = int(0)
        qtdtrocas2 = int(0)
        resultados2 = []

        for i in range(0, 300):
            slista = ""
            for i2 in range(0, 20):
                slista = slista + random.choice(string.ascii_letters)
            lista2.append(slista)

        for i in range(0, len(lista2)):
            for i2 in range(0, (len(lista2) - 1)):
                qtdcomparacoes2 += 1
                if lista2[i2] > lista2[i2 + 1]:
                    aux = lista2[i2]
                    lista2[i2] = lista2[i2 + 1]
                    lista2[i2 + 1] = aux
                    qtdtrocas2 += 1
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

    resultadosgeral = []
    resultadosgeral.append(difcomparacoes)
    resultadosgeral.append(diftroca)
    resultadosgeral.append(diftempo)

    return resultadosgeral
