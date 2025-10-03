num = int(input('Digite um número para conversão: '))

while True:
    
    print('''Escolha uma das bases numericas para conversão
      
      [1] converter para Binário
      [2] converter para Octal
      [3] converter para Hexadecimal
      [4] Trocar número
      [5] Sair''')

    opção = int(input('\nColoque sua opção: '))
    if opção == 1:
        print('{} convertido para binario é igual {}'.format(num, bin(num)))
    elif opção == 2:
        print('{} convertido para octal é igual {}'.format(num, oct(num)))
    elif opção == 3:
        print('{} convertido para hexadecimal é igual {}'.format(num, hex(num)))
    elif opção == 4: 
        num = int(input('Digite um número para conversão: '))
    elif opção == 5:
        break
    else:
        print('Opção invalida')
print('Programa encerrado')