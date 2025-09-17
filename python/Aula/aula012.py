nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo': 
    print('Que nome bonito')
elif nome == 'João' or nome =='Pedro' or nome == 'Rakin':
    print('Seu nome é bem popular no Brasil')
else:
    print('Que nome comum')
print('Tenha um bom dia, {}'.format(nome))