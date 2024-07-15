# Ler o número inteiro N
N = int(input("Digite um número inteiro entre 100 e 9999: "))

# Separar o algarismo das milhares
milhares = N // 1000
print("Milhares:", milhares)

# Atualizar N para conter apenas as centenas, dezenas e unidades
N = N % 1000

# Separar o algarismo das centenas
centenas = N // 100
print("Centenas:", centenas)

# Atualizar N para conter apenas as dezenas e unidades
N = N % 100

# Separar o algarismo das dezenas
dezenas = N // 10
print("Dezenas:", dezenas)

# Separar o algarismo das unidades
unidades = N % 10
print("Unidades:", unidades)
