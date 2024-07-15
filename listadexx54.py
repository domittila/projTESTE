# Leitura do número positivo pelo usuário
numero = int(input("Digite um número positivo: "))

# Inicialização da sequência Fibonacci
fibonacci = [0, 1]

# Cálculo da sequência Fibonacci até que o próximo número seja maior que 'numero'
while fibonacci[-1] <= numero:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)

# Impressão da sequência Fibonacci até o primeiro número superior a 'numero'
print("Sequência Fibonacci até o primeiro número superior ao número digitado:")
for num in fibonacci[:-1]:  # Excluir o último número que é maior que 'numero'
    print(num, end=" ")
print()
