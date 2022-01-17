# Tupla é uma lista imutavel representada pelo (   )
dimensoes = (200, 50)
print(dimensoes[0])
print(dimensoes[1])
print('')

# dimensoes2 = (100, 50)
# dimensoes2[0] = 250    # Erro de proposito pq tenta mudar a tupla e nao da pq ela é imutavel
# print(dimensoes2)

# Percorrendo todos valores de uma tupla com um laço
dimensoes3= (300, 100)
for dimensao3 in dimensoes3:
    print(dimensao3)
print('')

# Sobrescrevendo uma Tupla
dimensoes4 = (350, 150)
print("Dimensao original")
for dimensao4 in dimensoes4:
    print(dimensao4)
print('')

print('Dimensao modificada')
dimensoes4 = (450, 250)
for dimensao4 in dimensoes4:
    print(dimensao4)

