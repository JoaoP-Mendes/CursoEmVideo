print('-=-' * 30)
print('CALCULADORA')
print('-=-' * 30)


print('''Qual operação gostaria da fazer? 
    [ 1 ] - adição 
    [ 2 ] - subtração 
    [ 3 ] - divisão  
    [ 4 ] - multiplicação''')
rOperacao = str(input('Digite sua resposta: ')).strip()

#Lista de operadores
adição = ['adição', 'adicao', 'adiçao', 'adicão', '+', '1'] 
subtração = ['subtração', 'subtraçao', 'subtracão', 'subtracao', 'sub']
divisão = ['divisão', 'divisao', 'div', '3' ]


#Adição 
if rOperacao == adição[0] or rOperacao == '1': 
    qntNum = int(input('Com quantos números gostaria de fazer essa operação?\n '))
    contador = 0
    soma = 0

    while contador < qntNum: 
        num = int(input('Digite o {}º numero: '.format(contador + 1)))#Essa contador é para ficar ideal, já que começa no nº0 (estetica para o usuário)
        soma = soma + num
        contador = contador + 1 #Vai amarzenar a quantidade de vezes que já foi feita a operação
    print('O valor do calculo é {}'.format(soma))

"""#Subtração
if rOperacao == subtração[0]or rOperacao == '2':
    qntNum = int(input('Com quantos números gostaria de fazer essa opeção?\n '))
    contador = 0
    sub = 0
    while contador < qntNum:
        if qntNum > 2: 
            num = int(input('Digite o {}º número: '.format(contador + 1)))
            sub = sub - num
           resu = sub - (2 * sub) 
            contador += 1
        '''num = int(input('Digite o {}º número: '.format(contador + 1)))
        sub = num1 - num
        contador += 1'''
    print('O resultado é {}'.format(sub))"""

#Divisão 
if rOperacao == divisão[0] or rOperacao == '3':
    qntNum = int(input('Com quantos números gostaria de fazer essa operação? '))
    contador = 0
    div = 0

    while contador < qntNum:
        num = int(input('Digite o {}º número: '.format(contador + 1)))
        div = num * div
        contador = contador + 1
    print(div)