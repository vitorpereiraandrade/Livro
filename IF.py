cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Verificando diferenca
ingredientes = 'mushrooms'
if ingredientes != 'anchovas':
    print('Nao pediu anchovas')

resposta = 17
if resposta != 42:
    print('Essa resposta está incorreta.Tente outra vez')

# Verificando se um valor nao esta em uma lista

banidos = ['vitor', 'magaly', 'vini']
usuario = 'zion'
if usuario not in banidos:
    print(f'{usuario.title()}, Vc pode responder ao forum, não esta banido')





