"""nome = str(input('Qual é seu nome? ')).strip()
valor = float(input('{}, qual é o valor da casa? '.format(nome)))
salario = float(input('\nInforme seu salário atual: '))

anos = int(input('Em quantos anos gostaria de pagar a casa? '))
ConvParcela = anos * 12
valorParcela = valor / ConvParcela

if salario * 30 /100 >= valorParcela:
    print('\nO valor da parcela ficou R${:.2f} e será parcelado em {} vezes'.format(valorParcela, ConvParcela))
else :
    print('\nNão será possível fazer a parcela, o valor da parcela é maior que 30 porcento do seu salário')
    print('O valor das parcelas ficaram R${:.2f} x {} vezes, mais alto que 30 porcento do seu salário R${:.2}'.format(valorParcela, ConvParcela, salario))"""

nome = str(input('Digite seu nome: ')).strip()
while True:
    valor = float(input('Qual é o valor da casa R$? '))
    salario = float(input(f'{nome}, qual seu salário atualmente? '))

    anos = int(input('Em quantos anos você gostaria de pagar a casa? '))
    conveParcelas = anos * 12
    print(f'Em {anos} você pagaria {conveParcelas} Parcelas\n')
    valorParcela = valor / conveParcelas

    if salario * 30 / 100 >= valorParcela:
        print(f'Será possível financiar a casa, ficaram {conveParcelas} parcelas no valor de R${valorParcela}')
        break
    else: 
        salario30 = salario * 30 / 100
        print(f'Não será possível fazer a parcela dessa casa em {conveParcelas} vezes')
        print(f'O valor de uma parcela é maior que 30% do seu salário')
        print(salario30, valorParcela)
        