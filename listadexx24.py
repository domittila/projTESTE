# Inicializar a variável para armazenar a soma dos números
soma = 0

# Iterar de 1 até 999 (não inclui 1000)
for i in range(1, 1000):
    # Verificar se o número é múltiplo de 3 ou 5
    if i % 3 == 0 or i % 5 == 0:
        soma += i

# Exibir o resultado da soma
print(f"A soma de todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5 é: {soma}")
