"""
Introdução ao desempactoamento + tuples (tuplas)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
indices = range(len(lista))

print(indices)


for indice in indices:
    print(indice, lista[indice])