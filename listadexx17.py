def somaDosPrimeirosNaturais(n):
    # Verifica se n é um número inteiro positivo
    if n <= 0:
        print("n deve ser um número inteiro positivo.")
        return None
    
    # Calcula a soma dos n primeiros números naturais
    soma = n * (n + 1) // 2
    
    return soma

# Solicita ao usuário que digite o valor de n
n = int(input("Digite um número inteiro positivo n: "))

# Calcula a soma dos n primeiros números naturais
resultado = somaDosPrimeirosNaturais(n)

# Verifica se o resultado não é None antes de imprimir
if resultado is not None:
    print(f"A soma dos {n} primeiros números naturais é: {resultado}")
