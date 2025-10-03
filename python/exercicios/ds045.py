import random

contador_vitoria = 0
contador_derrota = 0

while True:

    print('-' * 35)
    print('''Suas opções: 
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA
        [ 3 ] Sair''')
    jogador = int(input('Qual será sua jogada? '))
    maquina = random.randint(0, 2)

    while jogador != 0 and jogador != 1 and jogador != 2 and jogador != 3:
         jogador = int(input('Qual será a jogada? '))
    if jogador == 3:
        break

    print('\nJO')
    print('KEN')
    print('PÔ')



    if maquina == 0 and jogador == 2:
        print('\nA Maquina ganhou!!')
        print('Maquina escolheu pedra e o jogador tesoura')
        contador_derrota += 1

    elif maquina == 1 and jogador == 0:
        print('\nA Maquina ganhou!!')
        print('Maquina escolheu papel e o jogador pedra')  
        contador_derrota += 1  

    elif maquina == 2 and jogador == 1:
        print('\nA Maquina ganhou!!')
        print('Maquina escolheu tesoura e o jogador papel')
        contador_derrota += 1

    elif maquina == 0 and jogador == 1:
        print('\nO jogador ganhou!!')
        print('Papel ganha de Pedra')
        contador_vitoria += 1

    elif maquina == 1 and jogador == 2: 
        print('\nO jogador ganhou!!')
        print('Tesoura ganha de Papel')
        contador_vitoria += 1

    elif maquina == 2 and jogador == 0:
        print('\nO jogador ganhou!!')
        print('Pedra ganha de Tesoura')
        contador_vitoria += 1

    elif maquina == 0 and jogador == 0:
        print('\nEMPATE, ambos escolheram os mesmos')

    elif maquina == 1 and jogador == 1:
        print('\nEMPATE, ambos escolheram os mesmos')

    elif maquina == 2 and jogador == 2:
        print('\nEMPATE, ambos escolheram os mesmos')

print('\nJOGO ENCERRADO!!')
if contador_derrota > contador_vitoria:
    print(f'A máquina ganhou com {contador_derrota} vitorias')
elif contador_derrota < contador_vitoria:
    print(f'O jogador ganhou com {contador_vitoria} vitorias')
elif contador_derrota == contador_vitoria:
    print(f'Ninguém vai ganhar ou perder, jogo empatado, jogador: {contador_vitoria} maquina: {contador_derrota}')
