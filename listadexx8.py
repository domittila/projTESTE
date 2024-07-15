def calculaMediaDezPositivos():
    soma = 0
    contador = 0
    
    while contador < 10:
        numero = int(input(f"Digite o {contador+1}º número inteiro positivo: "))
        if numero > 0:
            soma += numero
            contador += 1
        else:
            print("Número inválido. Digite apenas números inteiros positivos.")

    media = soma / 10
    return media

# Chama a função para calcular a média dos 10 números inteiros positivos
media = calculaMediaDezPositivos()
print(f"A média dos 10 números inteiros positivos digitados é: {media}")
