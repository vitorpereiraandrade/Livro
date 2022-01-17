jogadores = ['charles', 'martina', 'michael', 'florence', 'eli']
print(jogadores[0:3])
print(jogadores[1:4])
print(jogadores[2:])   # do 2 até o último item
print(jogadores[-3:])  # numero negativo devolve um elemento a uma determinada distancia do final da lista ex: TRES ULTIMOS
print('')

#Percorrendo uma fatia com um laço
jogadores2 = ['charles2', 'martina2', 'michael2', 'florence2', 'eli2']
print('Aqui está os 3 primeiros jogadores do meu time: ')
for jogador in jogadores2[:3]:
    print(jogador.title())

#Copiando uma lista
#Copiando uma lista toda [:] Isso diz a Python para criar uma lista que começa no primeiro item e termina no ultimo
# copiando a lista toda
minha_comida = ['pizza', 'batata', 'bolo de cenoura']
amigo_comida = minha_comida[:]
print('Minha comida favorita são: ')
print(minha_comida)
print('\nComida preferida do meu amigo são:')
print(amigo_comida)
print('')

minha_comida.append('cannoli')
amigo_comida.append('ice cream')
print(f'Minha comida: {minha_comida}')
print(f'Comida do amigo: {amigo_comida}')