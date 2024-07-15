# Ler a base (x) e o expoente (y) do usuário
x = int(input("Digite o valor da base (x): "))
y = int(input("Digite o valor do expoente (y): "))

# Inicializar a variável para armazenar o resultado da potência
resultado = 1

# Caso especial: se o expoente for 0, o resultado é sempre 1
if y == 0:
    resultado = 1
else:
    # Loop para calcular a potência
    for i in range(y):
        resultado *= x

# Exibir o resultado da potência
print(f"{x}^{y} = {resultado}")
