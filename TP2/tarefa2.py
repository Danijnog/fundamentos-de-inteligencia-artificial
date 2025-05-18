import random
from tabulate import tabulate  # Certifique-se de instalar a biblioteca tabulate

PENALIDADE = 1000  # Penalidade usada para desincentivar soluções que excedem a capacidade da mochila

def ler_arquivo_mochila(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        n_itens = int(f.readline().strip())
        capacidade = int(f.readline().strip())
        pesos = []
        valores = []
        for _ in range(n_itens+1):
            linha = f.readline().strip()
            if linha:  # Verifica se a linha não está vazia
                partes = linha.split()
                if len(partes) >= 2:  # Verifica se há pelo menos duas colunas
                    pesos.append(int(partes[0]))
                    valores.append(int(partes[1]))
                else:
                    raise ValueError(f"Linha inválida no arquivo: {linha}")
            else:
                continue  # Ignora linhas vazias
    return capacidade, pesos, valores

def calcular_fitness(individuo, pesos, valores, capacidade):
    peso_total = sum(pesos[i] for i in range(len(individuo)) if individuo[i] == 1)
    valor_total = sum(valores[i] for i in range(len(individuo)) if individuo[i] == 1)
    
    if peso_total > capacidade:
        # Penalização por exceder a capacidade
        return max(0, valor_total - (peso_total - capacidade) * PENALIDADE)
    else:
        return valor_total

def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1)-1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]  # Flip do bit
    return individuo

def algoritmo_genetico_mochila(capacidade, pesos, valores, tamanho_populacao=50, geracoes=100, taxa_mutacao=0.01):
    n_itens = len(pesos)
    
    # Inicialização da população
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = [random.randint(0, 1) for _ in range(n_itens)]
        populacao.append(individuo)
    
    for geracao in range(geracoes):
        # Avaliação
        fitness = [calcular_fitness(ind, pesos, valores, capacidade) for ind in populacao]
        
        # Seleção de pais (por exemplo, torneio)
        pais = selecao_por_torneio(populacao, fitness, tamanho_torneio=3)
        
        # Cruzamento e mutação
        nova_geracao = []
        for i in range(0, tamanho_populacao, 2):
            pai1, pai2 = pais[i], pais[i+1]
            filho1, filho2 = crossover(pai1, pai2)
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            nova_geracao.extend([filho1, filho2])
        
        populacao = nova_geracao
    
    # Retorna a melhor solução encontrada
    fitness = [calcular_fitness(ind, pesos, valores, capacidade) for ind in populacao]
    melhor_idx = fitness.index(max(fitness))
    return populacao[melhor_idx], fitness[melhor_idx]

def selecao_por_torneio(populacao, fitness, tamanho_torneio=3):
    pais = []
    for _ in range(len(populacao)):
        torneio = random.sample(list(zip(populacao, fitness)), tamanho_torneio)
        melhor = max(torneio, key=lambda x: x[1])
        pais.append(melhor[0])
    return pais

def main():
    capacidade, pesos, valores = ler_arquivo_mochila('C:\\Users\\alves.luiz\\Desktop\\Fund IA\\fundamentos-de-inteligencia-artificial\\TP2\\mochila.txt')
    melhor_solucao, melhor_fitness = algoritmo_genetico_mochila(capacidade, pesos, valores)
    melhor_fitness = float(melhor_fitness)
    peso_total = sum(pesos[i] for i in range(len(melhor_solucao)) if melhor_solucao[i] == 1)

    # Dados para a tabela principal
    tabela_principal = [
        ["Capacidade da mochila", capacidade],
        ["Valor total", melhor_fitness],
        ["Peso total", peso_total]
    ]

    # Dados para o grid de itens
    tabela_itens = []
    for i in range(len(melhor_solucao)):
        tabela_itens.append([
            f"Item {i + 1}",
            "Selecionado" if melhor_solucao[i] == 1 else "Não selecionado",
            pesos[i],
            valores[i]
        ])

    # Exibir a tabela principal
    print(tabulate(tabela_principal, headers=["Descrição", "Valor"], tablefmt="grid"))

    # Exibir o grid de itens
    print("\nItens:")
    print(tabulate(tabela_itens, headers=["Item", "Status", "Peso", "Valor"], tablefmt="grid"))

if __name__ == "__main__":
    main()