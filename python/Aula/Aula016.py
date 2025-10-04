lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutaveis
#lanche[1] = 'Refrigerante'

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

#print(len(lanche))
for comida in lanche:
    print(f'{comida}', end=', ')
print(f'Comi para caramba')