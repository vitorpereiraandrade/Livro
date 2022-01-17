nomes = ['Vitor', 'Maga', 'Vini', 'Zion', 'Zucky', 'Pescoço']
print(nomes[0:3])  # Os 3 primeiros nomes
print(nomes[1:4]) # Os 3 primeiros do meio
print(nomes[-3:])
print('')

minhas_pizzas = ['portuguesa', 'alho', 'calabresa', 'milho']
amigos_pizza = minhas_pizzas[:]
print(minhas_pizzas)
print(amigos_pizza)
minhas_pizzas.append('mignon')
print(minhas_pizzas)
amigos_pizza.append('frango')
print(amigos_pizza)
print('')

print('Minhas pizzas favoritas sao: ')
for minha_pizza in minhas_pizzas:
    print(minha_pizza.title())
print('')

print('As pizzas favoritas dos meu amigo sao: ')
for amigo_pizza in amigos_pizza:
    print(amigo_pizza.title())
print('')

comida = ['lasanha', 'pao', 'macarrao', 'picanha', 'batata frita', 'sorvete']
print('Minhas comidas preferidas sao: ')
for comidas in comida:
    print(comidas.title())
