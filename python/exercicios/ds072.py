numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desseseis', 'dessesete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número: '))
while n < 0 or n > 20:
    n = int(input('TENTE NOVAMENTE. Algo deu errado: '))

print(f'O número que você digitou foi {numero[n]}')