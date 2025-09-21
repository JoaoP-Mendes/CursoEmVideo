print('====== LOJA PORRA ======')
preço = float(input('Qual será o valor das compras? R$ '))
print('''Formas de pagamento
      
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão 
      [ 4 ] 3x ou mais no cartão ''')
opção = int(input('\nQual é a opção? '))
if opção == 1:
    desconto = preço - (preço * 10 / 100)

    print('\nO preço foi de R${:.2f} e com desconto de 10% foi para R${:.2f}'.format(preço, desconto))

elif opção == 2:
    desconto = preço - (preço * 5 / 100)

    print('\nO preço foi de R${:.2f} e com desconto de 5% foi para R${:.2f}'.format(preço, desconto))

elif opção == 3:
    print('\nA parcela ficará 2x de R${:.2f}'.format(preço / 2))

elif opção == 4:
    qntParcelas = int(input('Será parcelado em quantas vezes? '))
    if qntParcelas < 3:
        print('\nVocê pode parcelar em 2x e não será ccobrado nenhum juros')
    juros = preço + (preço * 20 / 100)
    print('\nO valor foi de R${:.2f} para R${:.2f}, ficando 3x de R${:.2f}'.format(preço, juros, juros / qntParcelas))