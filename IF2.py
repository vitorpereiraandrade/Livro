age = 19
if age >= 18:
    print('Voce pode votar')
    print('Voce ja se registrou para votar?')
print('')

age2 = 17
if age2 >= 18:
    print('Voce pode votar')
    print('Voce ja se registrou para votar?')
else:
    print('Sinto muito, voce nao tem idade suficiente pra votar')
    print('Tem que ser maior ou igual a 18 anos')
print('')

# IF - ELIF - ELSE
age3 = 12
if age3 < 4:
    print('Entrada gratuita')
elif age3 < 18:
    print('Entrada custa $5')
else:
    print('Entrada custa $ 10')
print('')

age4 = 12
if age4 < 4:
    price = 0
elif age4 < 18:
    price = 6
elif age4 < 65:
    price = 10
else:
    price = 5
print(f'O valor da entrada é ${price}')
print('')

#OMITINDO O BLOCO ELSE
age5 = 12
if age5 < 4:
    price = 0
elif age5 < 18:
    price = 5
elif age5 < 65:
    price = 5
print(f'O valor da entrada AGE5 é ${price}')
print('')

# TESTANDO VARIAS CONDICOES
ingredientes = ['cogumelo', 'queijo extra']
if 'cogumelo' in ingredientes:
    print('Adicionar cogumelos')
if 'peperoni' in ingredientes:
    print('Adicionar peperoni')
if 'queijo extra' in ingredientes:
    print('Adicionar queijo extra')
print('\nSua pizza está finalizada')



