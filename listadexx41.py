while True:
    # Ler o valor de R1 do usuário
    R1 = float(input("Digite o valor de R1 (ou 0 para sair): "))
    
    # Verificar se o usuário deseja sair
    if R1 == 0:
        print("Programa encerrado.")
        break
    
    # Ler o valor de R2 do usuário
    R2 = float(input("Digite o valor de R2 (ou 0 para sair): "))
    
    # Verificar se o usuário deseja sair
    if R2 == 0:
        print("Programa encerrado.")
        break
    
    # Calcular a resistência equivalente em paralelo
    Req = (R1 * R2) / (R1 + R2)
    
    # Exibir o resultado
    print(f"A resistência equivalente em paralelo de R1={R1} ohms e R2={R2} ohms é: {Req:.2f} ohms")
