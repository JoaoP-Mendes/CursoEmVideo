num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print("""\nO que gostaria de realizar com esses números?
      [ 1 ] - Somar 
      [ 2 ] - Multiplicar
      [ 3 ] - Maior 
      [ 4 ] - novos números
      [ 5 ] - Sair""")
resposta = int(input('Resposta: '))

while resposta != 5:
    if resposta == 1:
        soma = num1 + num2
        print('\nA soma dos dois números é {}'.format(soma))

    elif resposta == 2:
        mult = num1 * num2
        print('\nA resposta é {}'.format(mult))

    elif resposta == 3: 
        if num1 > num2: 
            print('\n{} é maior que {}'.format(num1, num2))
        elif num1 < num2:
            print('\n{} é maior que {}'.format(num2, num1))
        elif num1 == num2:
            print('\nOs números são iguais')

    elif resposta == 4:
        num1 = float(input('\nDigite um número: '))
        num2 = float(input('Digite outro número: '))
        
    resposta = int(input('O que gostaria de fazer agora? '))