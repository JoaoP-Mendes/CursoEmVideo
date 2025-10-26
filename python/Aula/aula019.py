#dados = {'nome':'Pedro', 'idade':25, }
#print(dados['nome'])
#dados['Sexo'] = 'M'
#print(f'nome: {dados['nome']}, idade: {dados['idade']} sexo: {dados['Sexo']}')
#del dados['idade']
#print(dados)

filme1 = {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}
filme2 = {'titulo':'Avengers', 'ano': 2012, 'diretor':'Joss whedon'}

#print(filme.values())
#print(filme.keys())
#print(filme.items())

#for k, v in filme.items():
#    print(f'O {k} é {v}')
locadora = [filme1, filme2]

filme3 = {}
filme3['titulo'] = input('Qual o nome do filme? ').strip()    
filme3['ano'] = input('Qual o ano do filme? ').strip()    
filme3['diretor'] = input('Qual o diretor do filme? ').strip()    
locadora.append(filme3)

filme = str(input('Qual filme quer ver? '))

for k, v in filme3.items():
    print(f'O {k} é {v}')