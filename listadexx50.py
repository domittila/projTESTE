def encontra_multiplos(n, i, j):
    multiplos = []
    count = 0
    numero = 0
    
    while count < n:
        if numero % i == 0 or numero % j == 0:
            multiplos.append(numero)
            count += 1
        numero += 1
    
    return multiplos

# Entrada de dados
n = int(input("Digite a quantidade de números naturais que deseja encontrar: "))
i = int(input("Digite o primeiro número inteiro positivo diferente de zero (i): "))
j = int(input("Digite o segundo número inteiro positivo diferente de zero (j): "))

# Chamada da função para encontrar os n primeiros naturais que são múltiplos de i ou de j
resultado = encontra_multiplos(n, i, j)

# Imprime o resultado em ordem crescente
print(f"Os {n} primeiros naturais que são múltiplos de {i} ou {j} (ou ambos) são: {resultado}")
