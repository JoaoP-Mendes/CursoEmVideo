import random

computador = random.randint (0, 10)
print('-=-' * 25)
print('Tente adivinhar o número que pensei')
print('-=-' * 25)


jogador = int(input('\nTente adivinhar o número que pensei 0 a 10: '))
jogadas = 1
while jogador != computador:
    jogador = int(input('Errou! Tente de novo: '))
    jogadas += 1
print('\nParabens, o número que pensei foi {}, foi preciso {} jogadas'.format(computador, jogadas))