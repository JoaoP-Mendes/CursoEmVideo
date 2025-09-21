import random
print('''Suas opções: 
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual será sua jogada? '))
maquina = random.randint(0, 2)

print('\nJO')
print('KEN')
print('PÔ')


if maquina == 0 and jogador == 2:
    print('\nA Maquina ganhou!!')
    print('Maquina escolheu pedra e o jogador tesoura')

elif maquina == 1 and jogador == 0:
    print('\nA Maquina ganhou!!')
    print('Maquina escolheu papel e o jogador pedra')    

elif maquina == 2 and jogador == 1:
    print('\nA Maquina ganhou!!')
    print('Maquina escolheu tesoura e o jogador papel')

elif maquina == 0 and jogador == 1:
    print('\nO jogador ganhou!!')
    print('Papel ganha de Pedra')

elif maquina == 1 and jogador == 2: 
    print('\nO jogador ganhou!!')
    print('Tesoura ganha de Papel')

elif maquina == 2 and jogador == 0:
    print('\nO jogador ganhou!!')
    print('Pedra ganha de Tesoura')

elif maquina == 0 and jogador == 0:
    print('\nEMPATE, ambos escolheram os mesmos')

elif maquina == 1 and jogador == 1:
    print('\nEMPATE, ambos escolheram os mesmos')

elif maquina == 2 and jogador == 2:
    print('\nEMPATE, ambos escolheram os mesmos')

else:
    print('\nEscolha uma jogada válida')