# Inicialização dos contadores
total = 0
pares = 0

# Loop principal
while True:
    # Ler um número inteiro do usuário
    num = int(input("Digite um número inteiro (0 para encerrar): "))
    
    # Verificar se o número digitado é zero para encerrar o loop
    if num == 0:
        break
    
    # Incrementar o contador de dados lidos
    total += 1
    
    # Verificar se o número é par
    if num % 2 == 0:
        pares += 1

# Informar o resultado
print(f"Número total de dados lidos: {total}")
print(f"Número de valores pares: {pares}")
