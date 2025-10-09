times = ('São Paulo', 'Atletico-MG', 'Flamengo', 'Grêmio', 'Fluminense', 'Internacional', 'Palmeiras', 'Santos', 'Ceará', 'Fortaleza', 'Corinthians', 'Athletico-PR', 'Bahia', 'Bragantino', 'Atlético-GO', 'Sport', 'Vasco', 'Coritiba', 'Botafogo', 'Goiás')

print('Tabela da Série A 2020')
print('''O que gostaria de verificar? 
      [1] - Os 5 primeiros times
      [2] - Os 4 últimos times
      [3] - Os times da tabela em ordem alfabetica
      [4] - Posição time\n''')

while True:
   escolha = int(input('Digite a resposta: '))
   while escolha > 4:   
      escolha = int(input('Algo deu errado. Tente novamente: '))
   
   if escolha == 1:
    for pos, time in enumerate(times[:5]):
       print(f'O {pos +1 }° colocado: {time}')

   elif escolha == 2:
      for time in times[-4:]:
         print(f'Os quatros últimos times são {time}')

   elif escolha == 3:
        print(f'{sorted(times)}')
   elif escolha == 4:
      busca = str(input('Coloque o time e faça a busca: ')).strip()
      print(f'{busca} está na {times.index(busca) + 1}° posição')
    