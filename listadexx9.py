def encontraMinMaxDezNumeros():
    menor = float('inf')  # Inicializa com um valor infinitamente grande
    maior = float('-inf') # Inicializa com um valor infinitamente pequeno
    
    for i in range(10):
        numero = float(input(f"Digite o {i+1}º número: "))
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
    
    return menor, maior

# Chama a função para encontrar o menor e o maior valor dentre os 10 números
menor, maior = encontraMinMaxDezNumeros()
print(f"O menor valor digitado é: {menor}")
print(f"O maior valor digitado é: {maior}")
