# Inicializar um vetor com 10 posições de números inteiros
vetor = [10, 5, 7, 2, 15, 20, 12, 8, 3, 18]

# Receber um novo valor do usuário
novo_valor = int(input("Digite um número para verificar se está no vetor: "))

# Verificar se o valor está presente no vetor
encontrado = False
for numero in vetor:
    if numero == novo_valor:
        encontrado = True
        break

# Exibir o resultado
if encontrado:
    print(f"O número {novo_valor} está presente no vetor.")
else:
    print(f"O número {novo_valor} não está presente no vetor.")
