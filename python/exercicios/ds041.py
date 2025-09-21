idade = int(input('Digite a idade do atleta: '))

if idade <= 9:
    print('O atleta entra na modalidade de Mirim.')
elif idade > 9 and idade <= 14:
    print('O atleta entra na modalidade de Infantil.')
elif idade > 14 and idade <= 19:
    print('O atleta entra na modalidade Júnior.')
elif idade > 19 and idade <= 25:
    print('O atleta entra na modalidade Senior')
elif idade > 25:
    print('O atleta entra na modalidade Master')