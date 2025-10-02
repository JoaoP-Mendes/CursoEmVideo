"""frutas = ["banana", "maça", "pera", "uva"]

for f in frutas:
    print(f)"""



"""nome = str(input('Qual seu nome? ')).strip() 
for letra in nome:
    print(letra, end='')"""

'''while True:
    numero = int(input('Digite um número par: '))
    if numero % 2 == 0:
        print('Obrigado!')
        break
    else:
        print('Seu burro, você digitou um número impar')'''

n = int(input('Digite um número par: '))
if n % 2 == 0:
    n = True #Fará o codigo ser executado
else:
    n = False #Fará o codigo não ser executado

while n: #Só vai funcionar ou não, dependendo da escolha do usuario 
    par = int(input('Coloque outro número par: '))
    if par % 2 == 0:
        print('Obrigado! ')
    else:
        break