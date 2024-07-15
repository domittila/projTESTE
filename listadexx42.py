import math

while True:
    # Ler o valor do usuário
    valor = float(input("Digite um valor (negativo ou zero para sair): "))
    
    # Verificar condição de saída
    if valor <= 0:
        print("Programa encerrado.")
        break
    
    # Calcular quadrado, cubo e raiz quadrada
    quadrado = valor ** 2
    cubo = valor ** 3
    raiz_quadrada = math.sqrt(valor)
    
    # Exibir os resultados
    print(f"Valor: {valor}")
    print(f"Quadrado: {quadrado}")
    print(f"Cubo: {cubo}")
    print(f"Raiz Quadrada: {raiz_quadrada}\n")
