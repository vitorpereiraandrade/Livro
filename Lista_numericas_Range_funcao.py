# Criando listas numericas
# Usando a funcao RANGE
for valor in range(1,5):
    print(valor)
print('')

for valor2 in range(1,6):
    print(valor2)

# Usando range para criar lista de numeros
numeros = list(range(1,6))
print(numeros)
print('')

# Numeros pares
numeros_pares = list(range(2,11,2))
print(numeros_pares)
print('')

#NUmeros elevados ao quadrado (**)

quadrados = []
for valor3 in range(1,11):
    quadrado = valor3 ** 2
    quadrados.append(quadrado)
print(quadrados)

# De modo mais conciso, omita a variavel temporaria "quadrado" e concatene cada novo valor diretamente na lista:
quadrados1 = []
for valor4 in range(1,11):
    quadrados1.append(valor4 ** 2)
print(quadrados1)

# Estatisticas simples com uma lista de numeros
digitos = [1,2,3,4,5,6,7,8,9,0]
print(min(digitos))     # numero minimo
print(max(digitos))     # numero maximo
print(sum(digitos))     # soma dos numeros

# List comprehensions
quadrados2 = [valor5 ** 2 for valor5 in range(1,11)]
print(quadrados2)
print('')