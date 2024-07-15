# Ler o valor inicial do intervalo
inicio = int(input("Digite o valor inicial do intervalo: "))

# Ler o valor final do intervalo
fim = int(input("Digite o valor final do intervalo: "))

# Verificar se o intervalo é válido
if inicio > fim:
    print("Intervalo inválido! O valor inicial deve ser menor ou igual ao valor final.")
else:
    # Inicializar variável para armazenar a soma dos números ímpares
    soma_impares = 0

    # Iterar através de todos os números no intervalo
    for num in range(inicio, fim + 1):
        # Verificar se o número é ímpar
        if num % 2 != 0:
            soma_impares += num

    # Exibir o resultado da soma dos números ímpares
    print(f"A soma dos números ímpares no intervalo [{inicio}, {fim}] é: {soma_impares}")
