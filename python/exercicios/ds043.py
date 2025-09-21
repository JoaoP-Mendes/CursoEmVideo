peso = float(input('Digite seu peso '))
altura = float(input('Digite sua Altura: '))
imc = peso / (altura ** 2)


if imc < 18.5:
    print('{:.1f}, abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('{:.1f}, peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('{:.1f}, sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('{:.1f}, obesidade'.format(imc))
elif imc > 40:
    print('{:.1f}, Obsesidade mórbida'.format(imc))