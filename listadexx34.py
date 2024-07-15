# Inicializar a lista para armazenar os 20 números inteiros
numeros = []

# Pedir ao usuário para digitar os 20 números e armazená-los na lista
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Inicializar listas para armazenar números pares e ímpares
par = []
impar = []

# Separar os números pares e ímpares
for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

# Exibir os três vetores
print("\nNúmeros digitados:")
print(numeros)
print("\nNúmeros pares:")
print(par)
print("\nNúmeros ímpares:")
print(impar)
