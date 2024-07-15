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

def soma_n_primos(n):
    """ Função para calcular a soma dos n primeiros números primos """
    soma = 0
    contagem = 0
    numero = 2  # Começamos a busca a partir do primeiro número primo
    
    while contagem < n:
        if eh_primo(numero):
            soma += numero
            contagem += 1
        numero += 1
    
    return soma

# Ler o valor de n do usuário
n = int(input("Digite um número inteiro não negativo n: "))

# Calcular a soma dos n primeiros números primos
resultado = soma_n_primos(n)

# Imprimir o resultado
print(f"A soma dos {n} primeiros números primos é: {resultado}")
