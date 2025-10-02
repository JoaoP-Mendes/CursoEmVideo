print('-' * 20)
print('CADASTRO DE PESSOAS')
print('-' * 20)


cIdade = 0
cHomem = 0
cMulher = 0

while True:
    idade = int(input('\nQual a idade? '))
    sexo = str(input('Qual o sexo? M/F: ')).upper().strip()

    while sexo != 'F' and sexo != 'M': 
            sexo = str(input('Qual o sexo? M/F: ')).upper().strip()
    
        
    if idade > 18:
         cIdade += 1
    if sexo == 'M':
         cHomem += 1
    if sexo == 'F' and idade < 20:
         cMulher += 1

    if sexo == 'F' or sexo == 'M':
        print('-'*20)
        escolha = str(input('Gostaria de fazer outro cadastro? S/N: ')).upper().strip()
        print('-'*20)

        if escolha == 'N':
             break
        
print(f'Foram cadastradas {cIdade} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {cHomem} homens.')
print(f'foram cadastradas {cMulher} mulheres com menos de 20 anos.')