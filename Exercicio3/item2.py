import random



vetor1 = []
vetor2 = []
vetor3 = []
max_vetor = 5
vetorG = []

for i in range(0, max_vetor):
    vetor1.append(random.randint(0, 100))

for i in range(0, max_vetor):
    vetor2.append(random.randint(0, 100))

for i in range(0, max_vetor):
    vetor3.append(random.randint(0, 100))

for i in range(0, max_vetor):
    vetorG.append(vetor1[i])
    vetorG.append(vetor2[i])
    vetorG.append(vetor3[i])

def mergesort(v, p, r):
    #condição de parada (condição de existência)
    if p < r:
        q = (p+r) // 2 #posição do elemento do meio
        mergesort(v, p, q) #quebrando o vetor em um sub-vetor 1 (metade da esquerda)
        mergesort(v, q+1, r) #quebrando o vetor em um sub-vetor 2 (metade da direita)
        intercalar(v, p, q, r)

def intercalar(v, p, q, r):
    temp = v.copy() #cópia vetor real
    i = p #contador do subvetor 1
    j = q+1 #contador do subvetor 2
    k = p #contador do vetor real

    #momento em que a intercalação será realizada
    while k <= r:
        if i > q:
            #entra quando não tiver mais elementos no subvetor 1
            v[k] = temp[j]
            j += 1
        elif j > r:
            #entra quando não tiver mais elementos no subvetor 2
            v[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]:
            #nesse caso, retirar o elemento do subvetor 1
            v[k] = temp[i]
            i += 1
        else:
            #nesse caso, retirar o elemento do sub-vetor 2
            v[k] = temp[j]
            j += 1
        k += 1

mergesort(vetorG, 0, len(vetorG)-1)

print(vetorG)