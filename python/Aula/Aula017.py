#valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
#print(valores)
#valores.append(int(input('Coloque um novo número: ')))
#print(valores)

a = [2, 3, 5, 8]
b = a[:]
b[2] = 8
print(a)
print(b)

#for c, v in enumerate(valores):
#    print(f'Na posição {c}, encontrei o valor {v}!')


'''nomes = ['João Paulo']
while True:
    printOpções
[ 1 ] - Ver lista de nome
[ 2 ] - Adiocionar mais nomes
[ 3 ] - Sair)
    decisao = int(input('Selecione a opção: '))

    if decisao == 1:
        for c, nome in enumerate(nomes):
            print(f'Nome: {nome} numero: {c + 1}º')

    elif decisao == 2:
        quantidadeNomes = int(input('Quantos nomes quer adicionar? '))
        for n in range(0, quantidadeNomes):
            nomes.append(str(input('Coloque o nome desejado: ')))

    elif decisao == 3:
        break

print(f'Muito obrigado! Volte sempre')
print(nomes)'''