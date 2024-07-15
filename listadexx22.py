# Inicialização das variáveis
soma_notas = 0
contador_notas = 0

# Loop para entrada de notas
while True:
    # Ler uma nota do usuário
    nota = float(input("Digite uma nota (entre 0 e 10, ou um valor negativo para sair): "))
    
    # Verificar se a nota é válida (entre 0 e 10)
    if 0 <= nota <= 10:
        # Adicionar a nota à soma das notas e incrementar o contador de notas
        soma_notas += nota
        contador_notas += 1
    else:
        # Se a nota não for válida, sair do loop
        break

# Verificar se foram digitadas notas válidas
if contador_notas > 0:
    # Calcular a média aritmética
    media = soma_notas / contador_notas
    print(f"A média das notas digitadas é: {media:.2f}")
else:
    print("Não foram digitadas notas válidas para cálculo da média.")

