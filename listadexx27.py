# Ler o valor inicial A do usuário
A = int(input("Digite um número inteiro para calcular o fatorial (A!): "))

# Inicializar variável para armazenar o resultado do fatorial
resultado = 1

# Inicializar string para armazenar a representação da sequência de multiplicação
sequencia = f"{A}! ="

# Calcular o fatorial
for i in range(A, 0, -1):
    resultado *= i
    sequencia += f" {i}"
    if i > 1:
        sequencia += " X"

# Exibir o resultado
sequencia += f" = {resultado}"
print(sequencia)
