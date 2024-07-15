# Inicializar lista para armazenar as médias dos alunos
medias = []

# Pedir as quatro notas de cada um dos 10 alunos
for aluno in range(1, 11):
    notas = []
    for nota_numero in range(1, 5):
        nota = float(input(f"Digite a nota {nota_numero} do aluno {aluno}: "))
        notas.append(nota)
    
    # Calcular a média do aluno
    media_aluno = sum(notas) / len(notas)
    medias.append(media_aluno)

# Contar quantos alunos têm média maior ou igual a 7.0
alunos_aprovados = 0
for media in medias:
    if media >= 7.0:
        alunos_aprovados += 1

# Imprimir o número de alunos com média maior ou igual a 7.0
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
