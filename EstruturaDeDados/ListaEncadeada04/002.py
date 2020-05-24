from ListaEncadeada04.funcoes import*

lista = ListaEncadeada()
dic_aux = {}
dic_aux2 = {}
lista_ordenação = []

def menu():
    while True:
        print("**MENU**\n"
              "1. Cadastrar os unfionarios;\n"
              "2. mostrar o funcionário com maior salario;\n"
              "3. mostrar a média salarial;\n"
              "4. mostrar quais funcionarios tem um salario superior a um valor definido;")

        escolha = int(input("Digite a opção escolhida: "))

        if escolha == 1:
            for a in range(0,5):
                pergunta1 = input("Digite o nome do funcionário: ")
                pergunta2 = int(input("Digite o valor do salario: "))
                dic_aux[pergunta1] = pergunta2
            print(dic_aux)

            for x in dic_aux:
                insere_no_inicio(lista, x)
            print(lista)

            for b in dic_aux:
                lista_ordenação.append(dic_aux[b])
                bubbleSort(lista_ordenação)
            print(lista_ordenação)

            for c in lista_ordenação:
                novoDic = getKeysByValue(dic_aux, c)
                for key in novoDic:
                    dic_aux2[key] = dic_aux[key]

        elif escolha == 2:
            print("O funcionario com maior salario é: {}.".format(novoDic[0]))

        elif escolha == 3:
            numero = 0
            for f in lista_ordenação:
                numero = numero + f

            print("A Média salarial é :{}.".format(numero/5))

        elif escolha == 4:
            list_aux = []
            valor_base = int(input("Digite o valor base do salário: "))
            for salario in dic_aux.values():
                if salario >= valor_base:
                    list_aux.append(salario)
                else:
                    pass
            print(list_aux)

            for valor in list_aux:
                new_dic = getKeysByValue(dic_aux, valor)
                for key in new_dic:
                    print(key, valor)


        elif escolha == 0:
            break

menu()
