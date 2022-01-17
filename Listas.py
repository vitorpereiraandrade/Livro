# Listas
bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles)
print('')

#Acessando elementos de uma lista
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[2])
print(bicycles[-1]) # Aqui é pra acessar ultimo elemento da lista
print(bicycles[-2]) # O penultimo item da lista
print(bicycles[-3]) # Antipenultimo item da lista e assim vai -4, -5, -6 sucessivamente
print('')

# Usando valores individuais de uma lista
bicycles2 = ['caloi', 'honda', 'monarque', 'trek', 'bili']
message = 'My first bicycle was a '
print(f'{message} {bicycles2[0].title()}')
message2 = 'My first bicycle was a ' + bicycles2[0].title() + '.'   # Aqui estamos usando a concatenação
print(message2)
print('')

# Modificando elementos de uma lista
motos = ['honda', 'ducati', 'yamaha', 'suzuki']
print(motos)
motos[0] = 'ducati'
print(motos)
print('')

#Concatenando elementos no final de uma lista
print(motos)
motos.append('Honda')   #append insere um elemento no final da lista
print(motos)
print('')

# Usando uma lista vazia
motos2 = []
print(motos2)
motos2.append('Ducati')
motos2.append('Suzuki')
motos2.append('Honda')
print(motos2)
print('')

#Inserindo elementos em uma lista
motos3 = ['Honda', 'Yamaha', 'Suzuki']
print(motos3)
motos3.insert(0, 'Ducati')      # Aqui vc usa o (insert) para escolher a posicao que vc quer escolher e colocar o elemento
print(motos3)
motos3.insert(3, 'Mobilete')
print(motos3)
print('')

# Removendo um item utilizando a instrucao (DEL)
motos4 = ['ducati4', 'honda4', 'suzuki4']
print(motos4)
del motos4[0]          # no modo DEL vc remove pra sempre, ele sai da lista
print(motos4)
del motos4[1]
print(motos4)
print('')

#Removendo um item utilizando o metodo (POP)
# o metodo POP remove o ultimo item de uma lista, mas permite que vc trabalhe com esse depois da remocao

moto5 = ['honda5', 'yamaha5', 'suzuki5']
print(moto5)
popped_moto5 = moto5.pop()   # A saida mostra que o valor 'suzuki5' foi removido do final da lista e agora esta
# armazenado na variavel popped_moto5
print(moto5)
print(popped_moto5)
print('')

# Suponha que as motocicletas da lista estejam armazenadas em ordem cronologica, de acordo com a epoca em que fomos
# seus proprietario. Se for esse o caso, podemos usar o metodo POP() para exibir uma informacao sobre a ultima motos
# que compramos.

motos6 = ['honda6', 'yamaha6', 'suzuki6']
last_owned = motos6.pop()
print(motos6)
print(f'Minha ultima moto que compramos foi {last_owned.title()}')
print('')

#Removendo itens de qualquer posicao em uma lista com POP()

motos7 = ['honda7', 'yamaha7', 'suzuki7']
print(motos7)
primeira_posicao = motos7.pop(0)
print(primeira_posicao)
print('')

###### Quando usar o metodo DEL e o POP - Quando quiser apagar um item de uma lista e esse item nao vai ser usado de modo
# algum, utilize a instrucao DEL - se quiser usar o item a medida que remove-lo utilize o metodo POP  ############

# Removendo um item de acordo com o valor
motos8 = ['honda8'.title(), 'yamaha8'.title(), 'suzuki8'.title()]
print(motos8)
motos8.remove('yamaha8'.title())  # Se conhecer apenas o valor do item que deseja remover use o metodo REMOVE()
print(motos8)
too_expensive = 'honda8'.title()
motos8.remove(too_expensive)
print(motos8)   # Agora aqui da pra mostrar o motivo que removemos a 'honda8'
print(f'Removemos a {too_expensive} pq ela nao presta')




