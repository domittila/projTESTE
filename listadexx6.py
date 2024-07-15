def somaDezValores():
    soma = 0
    for i in range(10):
        valor = float(input(f"Digite o {i+1}º valor: "))
        soma += valor
    
    return soma

# Chama a função para calcular a soma dos 10 valores
resultado = somaDezValores()
print(f"A soma dos 10 valores digitados é: {resultado}")
