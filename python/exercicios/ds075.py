valor = (int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')))
print(valor)

print(f'O 9 apareceu {valor.count(9)} vezes.')
if 3 in valor:
    print(f'O 3 apareceu pela primeira vez na {valor.index(3) + 1}° posição ')
else:
    print(f'O 3 não apareceu ')
print('Os valores pares digitados foram ', end=', ç')
for n in valor:
    if n % 2 == 0:
        print(n, end='')
