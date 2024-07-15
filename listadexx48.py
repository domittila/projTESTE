# Definir a lista fornecida
lista = [1, 1, 4, 5, 6, 7, 3, 2, 2, -1]

# Ler os números de entrada
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Contar as ocorrências na lista
ocorrencias = {
    num1: lista.count(num1),
    num2: lista.count(num2),
    num3: lista.count(num3)
}

# Imprimir os resultados
for num in (num1, num2, num3):
    print(f"{num}: ocorreu {ocorrencias[num]} vez{'es' if ocorrencias[num] > 1 else ''}")
