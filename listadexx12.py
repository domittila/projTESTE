def imprimeNumerosNaturaisAteN(N):
    # Garantindo que N seja positivo
    if N < 0:
        print("N deve ser um número inteiro positivo.")
        return
    
    # Loop para imprimir os números naturais de 0 até N
    for i in range(N + 1):
        print(i, end=' ')

# Solicita ao usuário que digite o valor de N
N = int(input("Digite um número inteiro positivo N: "))

# Chama a função para imprimir os números naturais de 0 até N
print(f"\nNúmeros naturais de 0 até {N}:")
imprimeNumerosNaturaisAteN(N)