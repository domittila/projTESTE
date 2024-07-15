def eh_primo(num):
    """ Função para verificar se um número é primo """
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 é primo
    if num % 2 == 0:
        return False  # Números pares maiores que 2 não são primos
    
    # Verificar divisibilidade a partir de 3 até a raiz quadrada de num
    limite = int(num ** 0.5) + 1
    for i in range(3, limite, 2):
        if num % i == 0:
            return False
    
    return True

# Ler os valores de a e b do usuário
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

# Inicializar contador de números primos
contador_primos = 0

# Contar números primos no intervalo [a, b]
for num in range(a, b + 1):
    if eh_primo(num):
        contador_primos += 1

# Imprimir o resultado
print(f"Existem {contador_primos} números primos entre {a} e {b}.")
