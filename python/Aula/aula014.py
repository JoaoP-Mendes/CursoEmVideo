'''r = 'S'
rn = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? ')).upper()
    rn +=1
print(n)'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('{} e {}'.format(par, impar))