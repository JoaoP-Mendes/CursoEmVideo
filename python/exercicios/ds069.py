contIdade = 0
contMen = 0
contWoYe = 0


while True:
    idade = int(input('Idade: '))
    s = str(input('Sexo M/F: ')).upper()
    conti = str(input('\nQuer continuar: S/N\n')).upper()
    if conti != 'S' or conti == 'N':
        while not conti:
                conti = str(input('\nQuer continuar: S/N\n')).upper()

    
    if idade > 18:
        contIdade += 1

    if s == 'M':
        contMen += 1

    if s == 'F' and idade < 20:
        contWoYe += 1


    elif conti == 'N':
        break
print(f'Tem {contIdade} pessoas, com mais de 18 anos')
print(f'Foram cadastrados {contMen} homens')
print(f'Foram cadastradas {contWoYe} mulheres com menos de 20 anos')


