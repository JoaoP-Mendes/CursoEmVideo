inicio = int(input('Gostaria de começar em qual número: '))
final = int(input('Até qual número? '))
condicao = str(input('Com alguma condição? (s/n)')).strip().lower()

if condicao == 's':
    condição = int(input('Qual condição? '))
    for num in range(inicio, final + 1, condição):
        print(num, end='')
else:
    for num in range(inicio, final + 1):
        print(num, end=', ')


