aluno = {}

aluno['Nome'] = str(input('Qual o seu nome? '))
aluno['Media'] = int(input(f'Média de {aluno['Nome']}: '))


if aluno['Media'] > 7 and aluno['Media'] <= 10:
    aluno['Situação'] = 'Aprovado'
elif aluno['Media'] < 7 and aluno['Media'] >= 0:
    aluno['Situação'] = 'Reprovado'

print(f'Nome é igual {aluno['Nome']}')
print(f'Média é igual {aluno['Media']}')
print(f'Situação é igual {aluno['Situação']}')

