while True:
    produto = str(input('Qual o nome do produto? ')).strip()
    preço = float(input('Qual é o preço? R$'))

    resp = ' '
    
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp == 'N':
            break

print('{:-^40}'.format('Fim do programa'))