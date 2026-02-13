num_int = input('Digite um número inteiro: ')

if num_int.isdigit():
    num_int = int(num_int)
    num_impar
elif num_int % 2 == 0:
    print('O número é par')
elif num_int % 2 != 0:
    print('O número é impar')
else:
    print('Você não digitou um número inteiro')


