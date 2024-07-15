def imprimeNumerosParesAteN(N):
    # Verifica se N é par
    if N % 2 != 0:
        print("N deve ser um número inteiro positivo par.")
        return
    
    # Loop para imprimir os números pares de 0 até N
    for i in range(0, N + 1, 2):
        print(i, end=' ')

# Solicita ao usuário que digite o valor de N
N = int(input("Digite um número inteiro positivo par N: "))

# Chama a função para imprimir os números pares de 0 até N em ordem crescente
print(f"\nNúmeros pares de 0 até {N} em ordem crescente:")
imprimeNumerosParesAteN(N)
