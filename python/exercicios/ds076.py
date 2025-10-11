palavras = (str(input('Escreva a palavra e veja as vogais: ')).strip(),
            str(input('Escreva a palavra e veja as vogais: ')).strip(),
            str(input('Escreva a palavra e veja as vogais: ')).strip())
for p in palavras:
    print(f'\nNa palavra {p.upper()}, temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')