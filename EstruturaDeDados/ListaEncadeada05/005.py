from funcoes import*

lista_numeros = []
lista_par_encadeada = ListaEncadeada()
lista_impar_encadeada = ListaEncadeada()
lista = []
lista_encadeada = ListaEncadeada()
lista2 = ListaEncadeada()

while len(lista_numeros) < 20:
    pergunta = int(input("Digite o numero:"))
    lista_numeros.append(pergunta)

for a in lista_numeros:
    numero = a%2
    if numero == 0:
        #numero par
        lista.append(a)
        insere_no_inicio(lista_par_encadeada, a)
        insere_no_inicio(lista2, a)

    else:
        #numero impar
        lista.append(a)
        insere_no_inicio(lista_impar_encadeada,a)
        insere_no_inicio(lista2, a)

print("lista dos numeros pares:", lista_par_encadeada)
print("lista dos numeros impares:", lista_impar_encadeada)
lista.sort()
print("lista não ordenda:", lista2)
print("deseja mostrar os numeros na ordem:\n"
      "1. crescente;\n"
      "2. decrescente;\n"
      "0. encerra o programa.")

while True:
    pergunta = int(input("Digite a opção desejada: "))
    if pergunta == 1:
        lista.reverse()
        for b in lista:
            insere_no_inicio(lista_encadeada, b)
        print(lista_encadeada)

    elif pergunta == 2:
        for c in lista:
            insere_no_inicio(lista_encadeada, c)
        print(lista_encadeada)

    elif pergunta == 0:
        break
