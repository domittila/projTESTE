def imprimeNPrimeirosImpares(N):
    contador = 0
    numero = 1
    
    while contador < N:
        if numero % 2 != 0:
            print(numero, end=' ')
            contador += 1
        numero += 1

# Solicita ao usuário que digite o valor de N
N = int(input("Digite um número inteiro N: "))

# Chama a função para imprimir os N primeiros números naturais ímpares
print(f"\nOs {N} primeiros números naturais ímpares são:")
imprimeNPrimeirosImpares(N)
