#pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
#print(f'O {pessoas["nome"]} tem {pessoas['idade']} anos')

#for k, v in pessoas.items():
#    print(f'O {k} é {v}')


estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print('-=-'*20)
for e in brasil:  # 'e' representa cada dicionário na lista
    for k, v in e.items():  # Corrigido: usar 'e' em vez de 'estado'
        print(f'O campo {k} tem valor {v}')  