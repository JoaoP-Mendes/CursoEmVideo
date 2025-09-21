print('Verificar triângulo')

a = float(input('Coloque o valor da primeira reta: '))
b = float(input('Coloque o valor da segunda reta: '))
c = float(input('Coloque o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('\nAs retas podem formar um triângulo.')

    if a == b == c:
        print('\nEquilatero')
    elif a == b or a == c or b == c:
        print('\nIsóceles')
    else:
        print('\nESCALENO')

else:
    print('As retas não podem formar um triâgulo')