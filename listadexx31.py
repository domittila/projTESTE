# Salário inicial em 2019
salario = 4000

# Aumento em 2020 (1.5%)
aumento_2020 = salario * 0.015
salario += aumento_2020

# Aumentos a partir de 2021 (dobro do aumento do ano anterior)
aumento_anterior = aumento_2020
for ano in range(2021, 2024):  # calculando até 2023
    aumento_atual = aumento_anterior * 2
    salario += aumento_atual
    aumento_anterior = aumento_atual

# Exibir o salário atual do funcionário em 2023
print(f"O salário atual do funcionário em 2023 é R$ {salario:.2f}")

