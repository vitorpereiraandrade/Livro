car = 'subaru'
print('Se car for == subaru? Entao é True')
print(car == 'subaru')
print('\ncar for == bmw? Entao é False ')
print(car == 'bmw')

name = 'Vitor'
print('\nSe name == Vitor? Entao é True')
print(name == 'Vitor')
print('\nSe name == Vini? Entao é False')
print(name == 'Vini')

cor = 'amarelo'
print('\nSe cor for != de Branco? Entao é True')
print(cor != 'Branco')
print('\nSe cor for != de Amarelo? Entao é False')
print(cor != 'amarelo')
print('')

# teste de igualdade
nome = 'Vitor'
if nome == 'Vitor':
    print(nome == 'Vitor')
print('')

nome2 = 'maga'
print(nome2 != 'vitor')
print(nome2 == 'maga')
print(nome2 != 'maga')
print('')

nome3 = 'Vitor'
print(nome3.lower() == 'vitor')
print('')

age = 18
age_0 = 21
print(age >= 30 and age_0 <= 30)
print(age >= 30 or age_0 <= 30)
print('')

listas = ['vitor', 'vini', 'maga']
permissao = 'zion'
print('vitor' in listas)
print('zion' in listas)
if permissao not in listas:
    print(f'Sr. {permissao.title()} esta liberado')













