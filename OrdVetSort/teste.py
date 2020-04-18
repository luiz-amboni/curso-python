import random
import string


lista = []

for i in range(0, 10):
    slista = ""
    for i2 in range(0, 20):
        slista = slista + random.choice(string.ascii_letters)
    lista.append(slista)

print(lista)

