# Ordenando uma lista - Ordem alfabetica SORT
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
print('')                               # No SORT a lista fica na ordem alfabetica de forma PERMANENTE

#Ordem alfabetica inversa
cars.sort(reverse=True)
print(cars)
print('')

# Ordenando uma lista TEMPORARIAMENTE com a função SORTED()
cars2 = ['bmw2', 'audi2', 'toyota2', 'subaru2']
print('Esta é a ordem original:')
print(cars2)
print('\nAqui é a ordem em SORTED: ')
print(sorted(cars2))
print('\nVoltando ao normal:')
print(cars2)
print(sorted(cars2, reverse=True))   # Agora nao ordem alfabetica REVERSA
print('')

#Exibindo uma lista em ordem inversa     REVERSE()
cars3 = ['bmw3', 'audi3', 'toyota3', 'subaru3']
cars3.reverse()                 # O REVERSE inverte a ordem da lista, mas sem colocar alfabetica
print(cars3)                    # O REVERSE muda a ordem da lista permanente
print('')

# Descobrindo o tamanho de uma lista LEN
cars3 = ['bmw3', 'audi3', 'toyota3', 'subaru3']
print(len(cars3))










