#Método de ordenar vetor.
lista = [5]
for c in range(0, 13):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adiciona no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
