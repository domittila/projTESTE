# Função para calcular a média das notas sem a melhor e pior nota
def calcular_media_notas(notas):
    melhor_nota = max(notas)
    pior_nota = min(notas)
    
    # Removendo a melhor e pior nota
    notas.remove(melhor_nota)
    notas.remove(pior_nota)
    
    # Calculando a média das notas restantes
    media = sum(notas) / len(notas)
    return media, melhor_nota, pior_nota

# Programa principal
if __name__ == "__main__":
    # Leitura do nome do atleta
    nome_atleta = input("Digite o nome do atleta: ")
    
    # Leitura das notas dos jurados
    notas = []
    for i in range(7):
        nota = float(input(f"Digite a nota do jurado {i+1}: "))
        notas.append(nota)
    
    # Chamada da função para calcular média, melhor e pior nota
    media, melhor_nota, pior_nota = calcular_media_notas(notas)
    
    # Impressão dos resultados
    print("\nResultado final:")
    print(f"Atleta: {nome_atleta}")
    print(f"Melhor nota: {melhor_nota}")
    print(f"Pior nota: {pior_nota}")
    print(f"Média: {media:.1f}")
