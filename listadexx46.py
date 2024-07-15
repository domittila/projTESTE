# Alturas iniciais (em metros)
altura_chico = 1.70
altura_ze = 1.20

# Taxas de crescimento anual (em metros)
crescimento_chico = 0.02  # 2 centímetros por ano = 0.02 metros por ano
crescimento_ze = 0.03  # 3 centímetros por ano = 0.03 metros por ano

# Inicialização do contador de anos
anos = 0

# Enquanto a altura de Zé for menor ou igual à altura de Chico
while altura_ze <= altura_chico:
    # Atualiza as alturas com o crescimento anual
    altura_chico += crescimento_chico
    altura_ze += crescimento_ze
    
    # Incrementa o contador de anos
    anos += 1

# Imprime o número de anos necessários para Zé ser maior que Chico
print(f"São necessários {anos} anos para que Zé seja maior que Chico.")
