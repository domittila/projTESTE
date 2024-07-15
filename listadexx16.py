def imprimeNumerosImparesAteN(N):
    # Verifica se N é ímpar
    if N % 2 == 0:
        print("N deve ser um número inteiro positivo ímpar.")
        return
    
    # Loop para imprimir os números ímpares de 1 até N
    for i in range(1, N + 1, 2):
        print(i, end=' ')

# Solicita ao usuário que digite o valor de N
while True:
    N = int(input("Digite um número inteiro positivo ímpar N: "))
    if N > 0 and N % 2 != 0:
        break
    else:
        print("Número inválido. Digite um número inteiro positivo ímpar.")

# Chama a função para imprimir os números ímpares de 1 até N em ordem crescente
print(f"\nNúmeros ímpares de 1 até {N} em ordem crescente:")
imprimeNumerosImparesAteN(N)
