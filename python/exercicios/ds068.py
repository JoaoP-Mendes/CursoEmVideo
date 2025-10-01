import random

print('-=-'*10)
print('JOGO DE PAR OU IMPAR')
print('-=-'*10)

jN = int(input('Digite um valor: '))
computador = random.random(0,20)
jIP = str('Par ou impar? [P/I]').upper()
cont = 0

if jIP == 'P':
    cIP = 'I'
    if jN + computador % 2 == 0: 
        print('Jogador venceu')
    else:
        print('Maquina venceu')


elif jIP == 'I':
    cIP = 'P'