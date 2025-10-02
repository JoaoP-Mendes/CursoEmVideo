"""for tab in range(5, 10):
    print('Tabuada do {}'.format(tab))
    for tabu in range(0, 11):
         print('{} x {} = {}'.format(tab, tabu, tabu * tab))
    print('----------------')"""

"""c = 0
while c <= 10:
    print(f'{c}', end='')
    c += 1"""

"""tab = int(input('Verificar tabuada de: '))
"""
"""for c in range(0, 11):
    print(f'{tab} x {c} = {tab * c}')"""

vez = 1
while True:
    tab = int(input('Verificar tabuada de: '))

    while vez <= 10:
        r = tab * vez
        print(f'{tab} x {vez} = {r}')
        vez += 1
     
    if tab == 0:
        break    