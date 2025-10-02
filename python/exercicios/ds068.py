import random

print('-=-'*10)
print('JOGO DE PAR OU IMPAR')
print('-=-'*10)

cont = 0
while True:
    computador = random.randint(0,20)
    n = int(input('Digite um valor: '))
    jIP = str(input('Par ou impar? [P/I]')).upper().strip()
    

    print('-' * 30)
    if jIP == 'P':
        if n + computador % 2 == 0: 
            print(f'Jogador escolheu {n} e o comp {computador}, {n} + {computador} = ')
            print(f'{n + computador}')
            print('Jogador venceu!\n')
            cont += 1
        else:
            print(f'Jogador escolheu {n} e maquina {computador}, {n} + {computador} = ')
            print(f'{n + computador}')
            print('Maquina venceu')
            break
            
            
    if jIP == 'I':
        if n + computador % 2 == 0: 
            print(f'Jogador escolheu {n} e maquina {computador}, {n} + {computador} = ')
            print(f'{n + computador}')
            print('Maquina venceu!')
            break
        else:
            print(f'Jogador escolheu {n} e maquina {computador}, {n} + {computador} = ')
            print(f'{n + computador}')
            print('Jogador venceu!\n')
            cont += 1
    print('-' * 30)

print(f'O jogador venceu {cont} vezes')