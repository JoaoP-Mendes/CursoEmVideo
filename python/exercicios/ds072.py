while True:

    numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desseseis', 'dessesete', 'dezoito', 'dezenove', 'vinte')

    n = int(input('Digite um número: '))
    while n < 0 or n > 20:
        n = int(input('TENTE NOVAMENTE. Algo deu errado: '))

    print(f'O número que você digitou foi {numero[n]}')
    decisao = str(input('Quer fazer outro número? S/N ')).upper().strip()
    while decisao not in 'SN':
        decisao = str(input('Algo deu errado. Quer fazer outro número? S/N ')).upper().strip()
    if decisao == 'S':
        continue
    elif decisao == 'N':
        break
print('OBRIGADO, VOLTE SEMPRE')