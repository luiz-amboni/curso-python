from funcoes import*
lista_encadeada_padrao = ListaEncadeada()
lista_encadeada1 = ListaEncadeada()
lista_encadeada2 = ListaEncadeada()
lista_encadeada3 = ListaEncadeada()
lista_encadeada4 = ListaEncadeada()
lista_encadeada5 = ListaEncadeada()

lista_nomes = ["Luiz", "Pedro", "João", "Henrique", "Marcela"]
lista_notas = [7, 8, 9.5, 4, 5.5]
lista_aprovados = []

while len(lista_nomes) < 5:
    nome = input("Digite o nonme do aluno: ")
    nota = float(input("Digite a nota do aluno "))
    lista_nomes.append(nome)
    lista_notas.append(nota)

insere_no_inicio(lista_encadeada1, lista_notas[0])
insere_no_inicio(lista_encadeada1, lista_nomes[0])
insere_no_inicio(lista_encadeada2, lista_notas[1])
insere_no_inicio(lista_encadeada2, lista_nomes[1])
insere_no_inicio(lista_encadeada3, lista_notas[2])
insere_no_inicio(lista_encadeada3, lista_nomes[2])
insere_no_inicio(lista_encadeada4, lista_notas[3])
insere_no_inicio(lista_encadeada4, lista_nomes[3])
insere_no_inicio(lista_encadeada5, lista_notas[4])
insere_no_inicio(lista_encadeada5, lista_nomes[4])

insere_no_inicio(lista_encadeada_padrao,lista_encadeada5)
insere_no_inicio(lista_encadeada_padrao,lista_encadeada4)
insere_no_inicio(lista_encadeada_padrao,lista_encadeada3)
insere_no_inicio(lista_encadeada_padrao,lista_encadeada2)
insere_no_inicio(lista_encadeada_padrao,lista_encadeada1)
print(lista_encadeada_padrao)

cont = 0
for x in lista_notas:

    if x >= 7:
        formato = ("aluno: {}, Nota: {} : APROVADO".format(lista_nomes[cont], x))
        print(formato)
        lista_aprovados.append(formato)
        cont +=1

    elif x < 7:
        cont +=1

if len(lista_aprovados) == 0:
    print("nenhum aluno aprovado")
