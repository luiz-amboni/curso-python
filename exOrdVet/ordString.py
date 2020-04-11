#Método de ordenar vetor com Strings.
def ordstring(menuCresDesc):
    lista = []

    for c in range(0, 13):
        nome = input('Digite um nome: ')
        lista.append(nome)

    for c in range(0, len(lista)):
        for c2 in range(0, len(lista)):
            if lista[c] < lista[c2]:
                aux = lista[c]
                lista[c] = lista[c2]
                lista[c2] = aux

    if menuCresDesc == 2:
        lista.reverse()

    for c in range(0, len(lista)):
        print(f'{lista[c]}')
