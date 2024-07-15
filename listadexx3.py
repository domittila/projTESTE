import random

def sorteiaAluno(qtd_alunos):
    alunos = []
    
    # Solicitar nomes dos alunos
    for i in range(qtd_alunos):
        while True:
            nome = input(f"Digite o nome do aluno {i+1}: ").strip()
            if nome:
                alunos.append(nome)
                print(f"Nome '{nome}' adicionado com sucesso.")
                break
            else:
                print("Nome inválido. Por favor, digite um nome válido.")
    
    # Verifica se a lista de alunos não está vazia
    if not alunos:
        return "Nenhum aluno fornecido"
    
    # Sortear um aluno aleatoriamente
    aluno_sorteado = random.choice(alunos)
    
    # Retornar o aluno sorteado
    return aluno_sorteado

# Exemplo de uso da função sorteiaAluno()
quantidade = 6
primeiro_aluno = sorteiaAluno(quantidade)
print(f"O primeiro aluno(a) a apresentar será: {primeiro_aluno}")
