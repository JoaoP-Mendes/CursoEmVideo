from datetime import date
atual = date.today().year
nasc = int(input('Coloque o ano de nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos de idade em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Você está com idade para fazer o alistamento')
elif idade < 18:
    saldo = 18 - idade
    print('Falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}')
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento deviria ter sido em {}')