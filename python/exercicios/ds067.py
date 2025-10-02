while True:
    tab = int(input('Quer verificar a tabuada de qual valor? '))
    print('-' * 30)
    if tab < 0:
        break

    for c in range (1, 11):
        print(f'{tab} x {c} = {tab * c}')
    
    print('-' * 30)
"""while True:
    n = int(input('Digite um número e veja a sua tabuada: '))
    if n < 0:
        print('Programa encerrado')
        break

    print(f'Tabuada do {n}')
    c = 1
    while c <= 10:
        r = n * c
        print(f'{n} x {c} = {r}')
        c += 1"""