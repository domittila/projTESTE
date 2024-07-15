import random

# Gerar um número aleatório entre 1 e 100
numero_aleatorio = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número gerado entre 1 e 100.")

# Inicializar contador de tentativas
tentativas = 0

# Loop para permitir múltiplas tentativas
while True:
    # Solicitar ao usuário que faça um chute
    chute = int(input("Digite seu chute: "))
    
    # Incrementar o contador de tentativas
    tentativas += 1
    
    # Verificar se o chute é menor, maior ou igual ao número gerado
    if chute < numero_aleatorio:
        print("Chute menor que o número gerado. Tente novamente.")
    elif chute > numero_aleatorio:
        print("Chute maior que o número gerado. Tente novamente.")
    else:
        # Caso o chute seja igual ao número gerado
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
        break
