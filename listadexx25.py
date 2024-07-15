# Inicialização das variáveis
soma_idades = 0
contador_individuos = 0

# Loop para entrada das idades
while True:
    # Ler uma idade do usuário
    idade = int(input("Digite a idade (ou 0 para terminar): "))
    
    # Verificar se a idade é 0 para encerrar o loop
    if idade == 0:
        break
    
    # Adicionar a idade à soma das idades e incrementar o contador de indivíduos
    soma_idades += idade
    contador_individuos += 1

# Verificar se pelo menos uma idade foi digitada
if contador_individuos > 0:
    # Calcular a média das idades
    media_idades = soma_idades / contador_individuos
    print(f"A idade média do grupo é: {media_idades:.2f} anos")
else:
    print("Nenhuma idade foi digitada para calcular a média.")
