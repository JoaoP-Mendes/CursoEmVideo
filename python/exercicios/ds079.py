valor = []

while True:
    valor.append(int(input('Digite um valor: ')))
    if valor.append == valor:
        print('Valor duplicado, não será possível adicionar')
        valor.append = False
    decisao = str(input('Quer continuar? S/N ')).upper().strip()
    if decisao == 'S':
        continue
    elif decisao == 'N':
        break
print(valor)