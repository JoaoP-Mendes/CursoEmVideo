n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2 :
    print('O primeiro número digitado {} é maior que o segundo número {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número digitado {} é maior que o primeiro número {}'.format(n2, n1))
elif n1 == n2:
    print('Os dois números são iguais')