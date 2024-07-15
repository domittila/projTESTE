# Definição dos dados iniciais
salario_carlos = float(input("Digite o salário mensal de Carlos: "))
salario_joao = salario_carlos / 3
rendimento_poupanca = 0.02  # 2% ao mês
rendimento_renda_fixa = 0.05  # 5% ao mês

# Inicialização das variáveis
saldo_carlos = 0.0
saldo_joao = 0.0
meses = 0

# Calculando até o saldo de João ultrapassar ou igualar o de Carlos
while saldo_joao < saldo_carlos:
    # Atualiza os saldos com os rendimentos mensais
    saldo_carlos += salario_carlos
    saldo_carlos *= (1 + rendimento_poupanca)
    
    saldo_joao += salario_joao
    saldo_joao *= (1 + rendimento_renda_fixa)
    
    # Incrementa o contador de meses
    meses += 1

# Exibindo o resultado
print(f"João ultrapassará ou igualará Carlos em {meses} meses.")
