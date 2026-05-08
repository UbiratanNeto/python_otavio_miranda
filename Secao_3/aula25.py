"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Bira'
preco = 1000.95897643
variavel = '%s, o preço é R$%2.f' % (nome, preco)
print(variavel)
print('O hexadeciaml de %d é %08X' % (1500, 1500))