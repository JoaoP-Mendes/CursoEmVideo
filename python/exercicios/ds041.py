while True:
    idade = int(input('Digite a idade do atleta: '))

    if idade <= 9:
        print('O atleta entra na modalidade de Mirim.\n')
    elif idade > 9 and idade <= 14:
        print('O atleta entra na modalidade de Infantil.\n')
    elif idade > 14 and idade <= 19:
        print('O atleta entra na modalidade Júnior.\n')


    elif idade > 19 and idade <= 25:
        print('O atleta entra na modalidade Senior\n')    
    
    elif idade > 25:
        print('O atleta entra na modalidade Master.\n')

    verificar = str(input('Gostaria de verificar outro atleta? S/N ')).upper().strip()
    if verificar == 'S':
        print('Ok! Iniciando outra verificação\n')
    elif verificar == 'N':
        break

print('Programa encerrado! Volte sempre')