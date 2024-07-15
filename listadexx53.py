# Variáveis para armazenar estatísticas
idade_mais_velha = float('-inf')
idade_mais_nova = float('inf')
altura_mais_alto = float('-inf')
altura_mais_baixo = float('inf')
maior_peso = float('-inf')
soma_alturas = 0
soma_imcs = 0
count_masculino = 0
count_feminino = 0

# Leitura dos dados de 25 pessoas
for i in range(1, 26):
    print(f"Digite os dados da {i}ª pessoa:")
    
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))
    
    # Atualização das estatísticas
    if idade > idade_mais_velha:
        idade_mais_velha = idade
    if idade < idade_mais_nova:
        idade_mais_nova = idade
        
    if altura > altura_mais_alto:
        altura_mais_alto = altura
    if altura < altura_mais_baixo:
        altura_mais_baixo = altura
    
    if peso > maior_peso:
        maior_peso = peso
    
    soma_alturas += altura
    
    # Cálculo do IMC
    altura_metros = altura
    imc = peso / (altura_metros ** 2)
    soma_imcs += imc
    
    # Contagem de sexo masculino e feminino
    if sexo == 'M':
        count_masculino += 1
    elif sexo == 'F':
        count_feminino += 1
    else:
        print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")

# Cálculo da média de altura e de IMC
media_altura = soma_alturas / 25
media_imc = soma_imcs / 25

# Cálculo da porcentagem de sexo masculino e feminino
porcentagem_masculino = (count_masculino / 25) * 100
porcentagem_feminino = (count_feminino / 25) * 100

# Impressão dos resultados
print("\nResultados:")
print(f"a) Idade da pessoa mais velha: {idade_mais_velha} anos")
print(f"b) Idade da pessoa mais nova: {idade_mais_nova} anos")
print(f"c) Altura do mais alto: {altura_mais_alto:.2f} metros")
print(f"d) Altura do mais baixo: {altura_mais_baixo:.2f} metros")
print(f"e) Maior peso: {maior_peso} kg")
print(f"f) Média de Altura: {media_altura:.2f} metros")
print(f"   Média de IMC: {media_imc:.2f}")
print(f"g) Porcentagem de Sexo Masculino: {porcentagem_masculino:.2f}%")
print(f"h) Porcentagem de Sexo Feminino: {porcentagem_feminino:.2f}%")
