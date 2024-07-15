def somaDosPrimeirosNNumerosPares(N):
    soma = 0
    numero = 0
    count = 0
    
    while count < N:
        soma += numero
        numero += 2  # Avança para o próximo número par
        count += 1
    
    return soma

# Define o número de números pares que queremos somar
N = 50

# Chama a função para calcular a soma dos 50 primeiros números pares
soma = somaDosPrimeirosNNumerosPares(N)

# Exibe o resultado
print(f"A soma dos {N} primeiros números pares é: {soma}")
