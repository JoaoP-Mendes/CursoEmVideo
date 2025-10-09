from random import randint

numero = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
for n in numero:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(numero)}')
print(f'O menor número sorteado foi {min(numero)}')