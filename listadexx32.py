# Lista para armazenar os números digitados
numeros = []

# Pedir ao usuário para digitar 5 números e calcular a soma
soma = 0
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))  # Lê o número e converte para float
    numeros.append(numero)  # Adiciona o número à lista
    soma += numero  # Soma o número à variável soma

# Exibir a soma dos números digitados
print(f"\nA soma dos números digitados é: {soma}\n")

# Exibir os números digitados, um por linha
print("Números digitados:")
for num in numeros:
    print(num)
