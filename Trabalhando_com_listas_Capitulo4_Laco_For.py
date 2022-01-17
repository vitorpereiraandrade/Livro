#Percorrendo um lista inteira com um laço
# FOR
magicos = ['alice','david', 'carolina']
for magico in magicos:      # ' Para todo magico na lista de magicos, exiba o nome magico'
    print(magico)

magicos1 = ['alice1','david1', 'carolina1']
for magico1 in magicos1:
    print(f'{magico1.title()} é um ótimo mágico')
    print(f'Estamos ansiosos para ver o magico, {magico1.title()}\n')
print('Muito obrigado a todos os mágicos pelo show')