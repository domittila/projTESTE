# Inicialização das variáveis
soma = 0
quantidade = 0
maior = float('-inf')  # Inicializa com o menor valor possível
menor = float('inf')   # Inicializa com o maior valor possível
soma_pares = 0
quantidade_pares = 0

# Leitura dos números e cálculos
while True:
    numero = float(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break
    
    # Atualiza a soma e a quantidade de números
    soma += numero
    quantidade += 1
    
    # Atualiza o maior e o menor número
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    
    # Verifica se o número é par
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1

# Calcula a média geral dos números digitados
if quantidade > 0:
    media = soma / quantidade
else:
    media = 0  # Evita divisão por zero caso nenhum número seja digitado

# Calcula a média dos números pares, se houver algum número par digitado
if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0  # Se nenhum número par foi digitado

# Imprime os resultados
print(f"\n(a) Soma dos números digitados: {soma}")
print(f"(b) Quantidade de números digitados: {quantidade}")
print(f"(c) Média dos números digitados: {media:.2f}")
print(f"(d) Maior número digitado: {maior}")
print(f"(e) Menor número digitado: {menor}")
print(f"(f) Média dos números pares digitados: {media_pares:.2f}")
