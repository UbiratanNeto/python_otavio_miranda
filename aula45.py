"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = iter('Luiz') # Iterável #.__iter__()
# Iterador = iter(texto) #iterator

###
while True:
    try:
        letra = next(iterador)  #.__next__()
        print(letra)
    except StopIteration:
        break
###



###
for letra in texto:
    print(letra)