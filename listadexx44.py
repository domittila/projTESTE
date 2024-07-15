while True:
    # Apresentar o menu de opções
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    # Ler a opção do usuário
    opcao = int(input("Digite o número da operação desejada: "))
    
    # Verificar a opção escolhida
    if opcao == 5:
        print("Programa encerrado.")
        break
    elif opcao < 1 or opcao > 5:
        print("Opção inválida. Escolha uma opção de 1 a 5.")
        continue
    
    # Ler os dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Realizar a operação escolhida
    if opcao == 1:
        resultado = num1 + num2
        print(f"Resultado da adição: {resultado}")
    elif opcao == 2:
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    elif opcao == 3:
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")
    elif opcao == 4:
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
    
    print()  # Linha em branco para separar as operações
    
# Fim do programa
