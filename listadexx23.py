# Ler o número inteiro do usuário
numero = int(input("Digite um número inteiro positivo: "))

# Inicializar a variável para armazenar a soma dos divisores
soma_divisores = 0

# Iterar de 1 até a metade do número (pois não há divisores maiores que a metade)
for i in range(1, numero // 2 + 1):
    # Verificar se i é divisor de numero
    if numero % i == 0:
        soma_divisores += i

# Exibir o resultado
print(f"A soma dos divisores de {numero}, excluindo ele próprio, é: {soma_divisores}")
