import random
import string
import time


def ordsortchar():

    def ordvet1():

        lista1 = []
        qtdcomparacoes1 = int(0)
        qtdtrocas1 = int(0)
        resultados1 = []

        for i in range(0, 3000):
            lista1.append(random.choice(string.ascii_letters))

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

        for i in range(0, 5000):
            lista2.append(random.choice(string.ascii_letters))

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

    print('=' * 65)
    print(f'Quantidade de comparações Vet3000 VS Vet5000:   {resultados1[0]}   VS   {resultados2[0]}')
    print(f'\nQuantidade de trocas Vet3000 VS Vet5000:   {resultados1[1]}   VS   {resultados2[1]}')
    print(f'\nDiferença comparação:   {difcomparacoes}')
    print(f'Diferença troca:   {diftroca}')
    print(f'\nO tempo de execução dos vetores é de:   {tempovet1:.2f} s  VS   {tempovet2:.2f} s')
    print(f'\nA diferença de tempo de execução do vet1 para o vet2 é de:   {diftempo:.2f} s')
    print('=' * 65)

ordsortchar()