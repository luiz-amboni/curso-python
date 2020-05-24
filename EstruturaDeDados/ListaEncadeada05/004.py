from funcoes import*
class Funcionario:
    def __init__(self, nome = "sem nome", salario = 0, novo_salario = 0, porcentagem = 0):
        self.nome = nome
        self.salario = salario
        self.novo_salario = novo_salario
        self.porcentagem = porcentagem

def conta_salario(valor):
    if valor <= 850:
        Funcionario.novo_salario = valor
        return Funcionario.novo_salario
    elif valor > 850 and valor <= 1200:
        conta = valor - (valor * 0.1)
        Funcionario.novo_salario = conta
        return Funcionario.novo_salario
    elif valor > 1200:
        conta = valor - (valor * 0.2)
        Funcionario.novo_salario = conta
        return Funcionario.novo_salario

def conta_porcentagem(valor2):
    if valor2 <= 850:
        Funcionario.porcentagem = "isento de desconto"
        return Funcionario.porcentagem
    elif valor2 >850 and valor2 <= 1200:
        conta2 = valor2 * 0.1
        Funcionario.porcentagem = conta2
        return Funcionario.porcentagem
    elif valor2 >1200:
        conta2 = valor2 * 0.2
        Funcionario.porcentagem = conta2
        return Funcionario.porcentagem

nome = input("Digite o nome do primeiro funcionario: ")
salario = float(input("Digite o salario: "))
f1 = Funcionario(nome, salario)

nome = input("Digite o nome do funcionario: ")
salario = float(input("Digite o salario: "))
f2 = Funcionario(nome, salario)

nome = input("Digite o nome do funcionario: ")
salario = float(input("Digite o salario: "))
f3 = Funcionario(nome, salario)

nome = input("Digite o nome do funcionario: ")
salario = float(input("Digite o salario: "))
f4 = Funcionario(nome, salario)

nome = input("Digite o nome do funcionario: ")
salario = float(input("Digite o salario: "))
f5 = Funcionario(nome, salario)

nome = input("Digite o nome do funcionario: ")
salario = float(input("Digite o salario: "))
f6 = Funcionario(nome, salario)


f1.novo_salario = conta_salario(f1.salario)
f2.novo_salario = conta_salario(f2.salario)
f3.novo_salario = conta_salario(f3.salario)
f4.novo_salario = conta_salario(f4.salario)
f5.novo_salario = conta_salario(f5.salario)
f6.novo_salario = conta_salario(f6.salario)

f1.porcentagem = conta_porcentagem(f1.salario)
f2.porcentagem = conta_porcentagem(f2.salario)
f3.porcentagem = conta_porcentagem(f3.salario)
f4.porcentagem = conta_porcentagem(f4.salario)
f5.porcentagem = conta_porcentagem(f5.salario)
f6.porcentagem = conta_porcentagem(f6.salario)

lista_encadeada = ListaEncadeada()
lista_aux1 = ListaEncadeada()
lista_aux2 = ListaEncadeada()
lista_aux3 = ListaEncadeada()
lista_aux4 = ListaEncadeada()
lista_aux5 = ListaEncadeada()
lista_aux6 = ListaEncadeada()

lista_aux = []
lista_aux.append(f1.salario)
lista_aux.append(f2.salario)
lista_aux.append(f3.salario)
lista_aux.append(f4.salario)
lista_aux.append(f5.salario)
lista_aux.append(f6.salario)

lista_aux.sort()
lista_aux.reverse()

for x in lista_aux:
    if f1.salario == x:
        insere_no_inicio(lista_aux1,f1.salario)
        insere_no_inicio(lista_aux1,f1.nome)
        insere_no_inicio(lista_encadeada,lista_aux1)
    elif f2.salario == x:
        insere_no_inicio(lista_aux2,f2.salario)
        insere_no_inicio(lista_aux2,f2.nome)
        insere_no_inicio(lista_encadeada,lista_aux2)
    elif f3.salario == x:
        insere_no_inicio(lista_aux3,f3.salario)
        insere_no_inicio(lista_aux3,f3.nome)
        insere_no_inicio(lista_encadeada,lista_aux3)
    elif f4.salario == x:
        insere_no_inicio(lista_aux4,f4.salario)
        insere_no_inicio(lista_aux4,f4.nome)
        insere_no_inicio(lista_encadeada,lista_aux4)
    elif f5.salario == x:
        insere_no_inicio(lista_aux5,f5.salario)
        insere_no_inicio(lista_aux5,f5.nome)
        insere_no_inicio(lista_encadeada,lista_aux5)
    elif f6.salario == x:
        insere_no_inicio(lista_aux6,f6.salario)
        insere_no_inicio(lista_aux6,f6.nome)
        insere_no_inicio(lista_encadeada,lista_aux6)
print(lista_encadeada)

lista = []
lista.append(f1.novo_salario)
lista.append(f2.novo_salario)
lista.append(f2.novo_salario)
lista.append(f3.novo_salario)
lista.append(f4.novo_salario)
lista.append(f5.novo_salario)
lista.append(f6.novo_salario)

pergunta = int(input("Digite a ordem a ser mostrada:\n"
                     "1. crescente;\n"
                     "2. decrescente;\n"))
if pergunta == 1:
    lista.sort()
    for x in lista:
        if f1.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f1.nome,f1.novo_salario,f1.porcentagem))
        elif f2.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f2.nome,f2.novo_salario,f2.porcentagem))
        elif f3.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f3.nome,f3.novo_salario,f3.porcentagem))
        elif f4.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f4.nome,f4.novo_salario,f4.porcentagem))
        elif f5.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f5.nome,f5.novo_salario,f5.porcentagem))
        elif f6.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f6.nome,f6.novo_salario,f6.porcentagem))

elif pergunta == 2:
    lista.sort()
    lista.reverse()
    for x in lista:
        if f1.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f1.nome,f1.novo_salario,f1.porcentagem))
        elif f2.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f2.nome,f2.novo_salario,f2.porcentagem))
        elif f3.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f3.nome,f3.novo_salario,f3.porcentagem))
        elif f4.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f4.nome,f4.novo_salario,f4.porcentagem))
        elif f5.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f5.nome,f5.novo_salario,f5.porcentagem))
        elif f6.novo_salario == x:
            print("nome: {}, salario: {}, desconto: {}".format(f6.nome,f6.novo_salario,f6.porcentagem))


