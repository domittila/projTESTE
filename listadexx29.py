import math

# Função para calcular o MDC de dois números usando o Algoritmo de Euclides
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função para calcular o MMC de dois números usando o MDC
def lcm(a, b):
    return a * b // gcd(a, b)

# Calculando o MMC de uma lista de números
def lcm_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

# Definindo a lista de números de 1 a 20
numbers = list(range(1, 21))

# Calculando o MMC dos números de 1 a 20
result = lcm_multiple(numbers)

# Exibindo o resultado
print(f"O menor número divisível por todos os números de 1 a 20 é: {result}")
