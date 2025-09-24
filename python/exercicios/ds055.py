somaIdade = 0
mediaIdade = 0
maioridadehome = 0
nomevelho = ''
for p in range(1, 5):
    print('---------- {}ª pessoa ----------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade = somaIdade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome 
    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome

mediaIdade = somaIdade / 4
print('A média de idade do grupo é {} anos'.format(mediaIdade)) 
print('O homem mais velho é {} e tem {} anos'.format(nomevelho, maioridadehome))
    
