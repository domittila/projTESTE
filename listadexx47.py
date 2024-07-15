# Calcular a soma dos quadrados dos primeiros 100 números naturais
soma_quadrados = sum(x**2 for x in range(1, 101))

# Calcular o quadrado da soma dos primeiros 100 números naturais
soma = sum(range(1, 101))
quadrado_soma = soma ** 2

# Calcular a diferença entre o quadrado da soma e a soma dos quadrados
diferenca = quadrado_soma - soma_quadrados

# Imprimir os resultados
print(f"A soma dos quadrados dos primeiros 100 números naturais é: {soma_quadrados}")
print(f"O quadrado da soma dos primeiros 100 números naturais é: {quadrado_soma}")
print(f"A diferença entre o quadrado da soma e a soma dos quadrados é: {diferenca}")
