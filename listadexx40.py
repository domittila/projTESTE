# Solicitar ao usuário que digite o valor inicial e o valor final
valor_inicial = int(input("Digite o valor inicial do intervalo: "))
valor_final = int(input("Digite o valor final do intervalo: "))

# Verificar se o intervalo é válido
if valor_inicial > valor_final:
    print("Intervalo de valores inválido.")
else:
    # Inicializar variável para armazenar a soma dos números ímpares
    soma_impares = 0
    
    # Iterar através de todos os números no intervalo
    for num in range(valor_inicial, valor_final + 1):
        # Verificar se o número é ímpar
        if num % 2 != 0:
            soma_impares += num
    
    # Exibir o resultado da soma dos números ímpares
    print(f"Soma dos ímpares neste intervalo: {soma_impares}")
