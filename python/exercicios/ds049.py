num = int(input('Digite um número e verifique a tabuada: '))
for c in range(1,11):
    print('{} x {} = {}'.format(num, c, num*c))
print('\nEssa é a Tabuada do {}'.format(num))