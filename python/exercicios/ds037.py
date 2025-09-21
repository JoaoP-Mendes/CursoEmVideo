num = int(input('Digite um número para conversão: '))
print('''Escolha uma das bases numericas para conversão
      
      [1] converter para Binário
      [2] converter para Octal
      [3] converter para Hexadecimal''')
opção = int(input('\nColoque sua opão: '))
if opção == 1:
    print('{} convertido para binario é igual {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para octal é igual {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para hexadecimal é igual {}'.format(num, hex(num)))
else: 
    print('Opção invalida')