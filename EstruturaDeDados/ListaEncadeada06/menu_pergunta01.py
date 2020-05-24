from funcoes import*

lista1 = ListaEncadeada() #esta é a lista encadeada que eu vou utilizar
lista_aux1 = [] # essas listas auxiliares são para poder fazer as movimentações
lista_aux2 = [] # de informação e as trocas de valores
lista_aux3 = []
lista_aux4 = []
lista_aux5 = []
lista_aux = []
def menu():
    while True:
        print('**MENU**\n'
              '1. cadastar os produtos;\n'
              '2. mostrar os produtos;\n'
              '3. apresentar relatório;\n'
              '0. encerrar o programa;')

        escolha = int(input("Digite sua opção: "))

        # aqui eu pego as informações que a pessoa escreve e coloco nas listas auxiliares
        if escolha == 1:
            pergunta1 = int(input("Digite o codigo do produto: "))
            pergunta2 = int(input("Digite o preco do produto: "))
            pergunta3 = int(input("Digite a quanidade do produto: "))
            lista_aux1.append(pergunta1)
            lista_aux1.append(pergunta2)
            lista_aux1.append(pergunta3)
            lista_aux.append(pergunta2) # esse append aqui é feio para não perder a informação na hora de
                                        # transformar e poder limpar a lista encadeada no final

            pergunta1 = int(input("Digite o codigo do produto: "))
            pergunta2 = int(input("Digite o preco do produto: "))
            pergunta3 = int(input("Digite a quanidade do produto: "))
            lista_aux2.append(pergunta1)
            lista_aux2.append(pergunta2)
            lista_aux2.append(pergunta3)
            lista_aux.append(pergunta2)

            pergunta1 = int(input("Digite o codigo do produto: "))
            pergunta2 = int(input("Digite o preco do produto: "))
            pergunta3 = int(input("Digite a quanidade do produto: "))
            lista_aux3.append(pergunta1)
            lista_aux3.append(pergunta2)
            lista_aux3.append(pergunta3)
            lista_aux.append(pergunta2)

            pergunta1 = int(input("Digite o codigo do produto: "))
            pergunta2 = int(input("Digite o preco do produto: "))
            pergunta3 = int(input("Digite a quanidade do produto: "))
            lista_aux4.append(pergunta1)
            lista_aux4.append(pergunta2)
            lista_aux4.append(pergunta3)
            lista_aux.append(pergunta2)

            pergunta1 = int(input("Digite o codigo do produto: "))
            pergunta2 = int(input("Digite o preco do produto: "))
            pergunta3 = int(input("Digite a quanidade do produto: "))
            lista_aux5.append(pergunta1)
            lista_aux5.append(pergunta2)
            lista_aux5.append(pergunta3)
            lista_aux.append(pergunta2)

            # nesse momento eu coloco as informações na lista encadeada, na ordem inversa ( do final para o começo),
            insere_no_inicio(lista1,lista_aux5[2]) # para quando mostrar, ela ficar na ordem correta
            insere_no_inicio(lista1,lista_aux5[1])
            insere_no_inicio(lista1,lista_aux5[0])

            insere_no_inicio(lista1,lista_aux4[2])
            insere_no_inicio(lista1,lista_aux4[1])
            insere_no_inicio(lista1,lista_aux4[0])

            insere_no_inicio(lista1,lista_aux3[2])
            insere_no_inicio(lista1,lista_aux3[1])
            insere_no_inicio(lista1,lista_aux3[0])

            insere_no_inicio(lista1,lista_aux2[2])
            insere_no_inicio(lista1,lista_aux2[1])
            insere_no_inicio(lista1,lista_aux2[0])

            insere_no_inicio(lista1,lista_aux1[2])
            insere_no_inicio(lista1,lista_aux1[1])
            insere_no_inicio(lista1,lista_aux1[0])

        elif escolha == 2:
            print(lista1)

        elif escolha == 3:
            pergunta = int(input("digite qual a porcentagem de desconto (50%)"))
            transformacao = pergunta/100 # aqui eu faço a transformação do preco original do produto para ter o desconto
            lista_aux1[1] = lista_aux1[1] * transformacao
            lista_aux2[1] = lista_aux2[1] * transformacao
            lista_aux3[1] = lista_aux3[1] * transformacao
            lista_aux4[1] = lista_aux4[1] * transformacao
            lista_aux5[1] = lista_aux5[1] * transformacao

            # aqui eu removo todos os pontos da lista para poder adicionar com o novo valor
            remove(lista1,lista_aux1[0])
            remove(lista1,lista_aux[0])
            remove(lista1,lista_aux1[2])

            remove(lista1,lista_aux2[0])
            remove(lista1,lista_aux[1])
            remove(lista1,lista_aux2[2])

            remove(lista1,lista_aux3[0])
            remove(lista1,lista_aux[2])
            remove(lista1,lista_aux3[2])

            remove(lista1,lista_aux4[0])
            remove(lista1,lista_aux[3])
            remove(lista1,lista_aux4[2])

            remove(lista1,lista_aux5[0])
            remove(lista1,lista_aux[4])
            remove(lista1,lista_aux5[2])

            # aqui eu insiro todas as informações de novo , porem com o valor do preco atualizado
            insere_no_inicio(lista1,lista_aux5[2])
            insere_no_inicio(lista1,lista_aux5[1])
            insere_no_inicio(lista1,lista_aux5[0])

            insere_no_inicio(lista1,lista_aux4[2])
            insere_no_inicio(lista1,lista_aux4[1])
            insere_no_inicio(lista1,lista_aux4[0])

            insere_no_inicio(lista1,lista_aux3[2])
            insere_no_inicio(lista1,lista_aux3[1])
            insere_no_inicio(lista1,lista_aux3[0])

            insere_no_inicio(lista1,lista_aux2[2])
            insere_no_inicio(lista1,lista_aux2[1])
            insere_no_inicio(lista1,lista_aux2[0])

            insere_no_inicio(lista1,lista_aux1[2])
            insere_no_inicio(lista1,lista_aux1[1])
            insere_no_inicio(lista1,lista_aux1[0])

            print(lista1)
            # e aqui eu faço um contador de quantidade para mostrar quanto se tem no estoque no relatório
            contador_quantidade = lista_aux1[2] + lista_aux2[2] + lista_aux3[2] + lista_aux4[2] + lista_aux5[2]
            print(contador_quantidade)

        elif escolha == 0:
            break



menu()
