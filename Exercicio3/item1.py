def ordVetSelect():

    lista_nomes = []
    limite_max = 13
    posicao = 0

    while posicao < limite_max:
        nomes = input("Digite um nome para ser adicionado a lista:  ")
        posicao = posicao + 1
        lista_nomes.append(nomes)

    def ordListaNomesInsert(listaNomes):

        for i in range(1, len(listaNomes)):
            vAtual = listaNomes[i]
            posicao = i

            while posicao > 0 and listaNomes[posicao - 1] > vAtual:
                listaNomes[posicao] = listaNomes[posicao - 1]
                posicao = posicao - 1

            listaNomes[posicao] = vAtual

    ordListaNomesInsert(lista_nomes)
    print('Nomes em ordem alfabética: ', lista_nomes)
