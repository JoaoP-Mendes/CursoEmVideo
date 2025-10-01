vez = 1

while True:
    tab = int(input('Quer ver a tabada de qual valor? '))
    
    while vez <= 10:
        r = tab * vez
        print(f'{tab} x {vez} = {r}')
        vez += 1
    
    if tab < 0:
        break

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