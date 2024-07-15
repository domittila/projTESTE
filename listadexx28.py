# Exemplo de série alternada: S = 1 - 2 + 3 - 4 + 5
n = 5  # número de termos

S = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        S -= i
    else:
        S += i

print(f"O valor de S na série alternada é: {S}")
