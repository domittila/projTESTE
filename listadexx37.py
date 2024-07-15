import math

def verificar_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limite = int(math.sqrt(n)) + 1
    for divisor in range(3, limite, 2):
        if n % divisor == 0:
            return False
    
    return True

# Solicitar ao usuário que digite um número inteiro maior que 1
numero = int(input("Digite um número inteiro maior que 1: "))

# Verificar se o número é primo e imprimir o resultado
if verificar_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
