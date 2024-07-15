def calculaMediaDezInteiros():
    soma = 0
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        soma += numero
    
    media = soma / 10
    return media

# Chama a função para calcular a média dos 10 números inteiros
media = calculaMediaDezInteiros()
print(f"A média dos 10 números inteiros digitados é: {media}")
