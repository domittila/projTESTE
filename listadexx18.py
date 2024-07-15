def encontraMaiorNumero(qtd_numeros):
    if qtd_numeros <= 0:
        print("Quantidade de números deve ser maior que zero.")
        return
    
    maior_numero = float('-inf')  # Inicializa com um valor muito pequeno
    
    for i in range(qtd_numeros):
        numero = float(input(f"Digite o número {i+1}: "))
        if numero > maior_numero:
            maior_numero = numero
    
    return maior_numero

# Solicita ao usuário a quantidade de números
qtd_numeros = int(input("Digite a quantidade de números a serem lidos: "))

# Chama a função para encontrar o maior número
maior = encontraMaiorNumero(qtd_numeros)

# Imprime o maior número encontrado
print(f"O maior número digitado é: {maior}")

