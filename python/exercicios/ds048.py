print('========== VERIFICAÇÃO ==========')

num1 = int(input('Digite um numero impar: '))
num2 = int(input('Digite outro número impar: '))
soma = num1 + num2

if soma % 3 == 3 or soma % 3 == 1:
    print('A soma dos números {} são multiplos de 3, verifique na tabela:'.format(soma))
    for c in range(0, 501, 3):
        print(c)
elif soma % 3 != 3 or soma % 3 != 1:
    print('A soma não dos números {} não são multiplos de 3.'.format(soma))