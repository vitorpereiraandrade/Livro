for numero in range(1,21):
    print(numero)
print('')

numeros2 = list(range(1,1000001))
print(numeros2)
print('')

numeros3 = list(range(1,10000001))
print(max(numeros3))
print(min(numeros3))
print(sum(numeros3))
print('')

numero_impar = []
for valor in range(1,21,2):       # (1, 21, 2) comecando do numero 1 ate o 21 pulando de 2 em 2
    numero_impar.append(valor)
print(numero_impar)
print('')

multiplos_de_3 = []
for valor2 in range(3, 30, 3):      # Aqui estou fazendo multiplos de 3
    multiplos_de_3.append(valor2)
print(multiplos_de_3)
print('')

cubo = []
for valor3 in range(1,10):
    cubo.append(valor3 ** 3)   # Aqui estou fazendo o cubo de 1 a 9
print(cubo)
print('')

cubo_comprehension = [valor4 ** 3 for valor4 in range(1,10)]   # Aqui estou fazendo direto com o Comprehension
print(cubo_comprehension)









