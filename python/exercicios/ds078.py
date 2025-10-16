valor = []
maior = 0
menor = 0

for n in range(0, 5):
    valor.append(int(input(f'Digite um valor para posição {n}: ')))
    if n == 0:
        maior = menor = valor[n]
    else:
        if valor[n] > maior:
            maior = valor[n]
        if valor[n] < menor:
            menor = valor[n]


print(f'Os valores que você digitou foram {valor}')
print(f'O maior valor é {maior} na posição ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i} ...', end='')
print()
print(f'O maior valor é {menor} na posição ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i} ...', end='')


