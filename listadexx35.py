# Inicializar vetor para armazenar os 10 caracteres
caracteres = []

# Pedir ao usuário para digitar os 10 caracteres
for i in range(10):
    caractere = input(f"Digite o {i+1}º caractere: ")
    caracteres.append(caractere)

# Definir lista de consoantes (considerando letras minúsculas e maiúsculas)
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
              'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
              'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 
              'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

# Contar consoantes e imprimir
contador_consoantes = 0
consoantes_encontradas = []

for caractere in caracteres:
    if caractere in consoantes:
        contador_consoantes += 1
        consoantes_encontradas.append(caractere)

# Imprimir resultado
print(f"\nForam encontradas {contador_consoantes} consoantes.")
if contador_consoantes > 0:
    print("Consoantes encontradas:")
    for consoante in consoantes_encontradas:
        print(consoante)
