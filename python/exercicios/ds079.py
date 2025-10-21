valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor Duplicado! Não vou botar')

    r = str(input('Quer continuar? S/N '))
    if r in 'Nn':
        break
for valor in valores:
    print(valor)