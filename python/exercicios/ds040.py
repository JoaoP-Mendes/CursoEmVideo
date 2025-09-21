nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('\nAluno reprovado, média {:.2f}.'.format(media))
elif media > 5.0 and media < 6.9:
    print('\nAluno está de recuperação, média {:.2f}.'.format(media))
elif media > 6.9 and media < 10.0:
    print('\nAluno passsou! Média {:.2f}.'.format(media))
else:
    print('\nA media está errada, coloque novamente as notas, {:.2f}'.format(media))