import random
with open("lista.txt") as lista:
    linea = lista.readlines()
print(random.choice(linea))