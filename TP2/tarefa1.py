import numpy as np
import pandas as pd
import random
from typing import List, Tuple
import matplotlib.pyplot as plt

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, 
                 tournament_size, crossover_rate, 
                 elitism_count, max_generations):
        
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count
        self.max_generations = max_generations

        # Problema dado na tarefa
        self.num_variables = 10
        self.min_value = -5.0
        self.max_value = 5.0
    
    def initialize_population(self) -> List[np.ndarray]:
        """
        Inicializa a população com valores aleatórios dentro do intervalo.
        """
        population = [np.random.uniform(self.min_value, self.max_value, self.num_variables)
                for _ in range(self.population_size)]
        
        return population
    
    def evaluate_fitness(self, individual: np.ndarray) -> float:
        """
        Fitness do indivíduo da população.
        """
        return np.sum(individual**2)
    
    def tournament_selection(self, population: List[np.ndarray], fitness: List[float]) -> np.ndarray:
        """
        Seleção por torneio - escolhe o melhor entre k indivíduos aleatórios.
        """
        tournament = random.sample(list(zip(population, fitness)), self.tournament_size)

        return min(tournament, key=lambda x: x[1])[0]
    
    def roulette_selection(self, population: List[np.ndarray], fitness: List[float]) -> np.ndarray:
        """
        Seleção por roleta. Implementado para comparar com o seleção por torneio (método acima).
        """
        # Transforma fitness de minimização para maximização
        inverted_fitness = 1 / (1 + np.array(fitness))
        total_fitness = np.sum(inverted_fitness)
        probabilities = inverted_fitness / total_fitness

        # Seleciona um índice baseado nas probabilidades
        selected_idx = np.random.choice(len(population), p=probabilities)

        return population[selected_idx]
    
    def arithmetic_crossover(self, parent1, parent2) -> Tuple[np.ndarray, np.ndarray]:
        """
        Cruzamento aritmético para variáveis contínuas.
        """
        # Fator de mistura aleatório
        alpha = np.random.uniform(0, 1, self.num_variables)

        # Cria os filhos como combinações lineares dos pais
        child1 = alpha * parent1 + (1 - alpha) * parent2
        child2 = (1 - alpha) * parent1 + alpha * parent2

        return child1, child2
    
    def gaussian_mutation(self, individual: np.ndarray) -> np.ndarray:
        """
        Mutação gaussiana para variáveis contínuas.
        """
        mutaded = individual.copy()
        for i in range(self.num_variables):
            if random.random() < self.mutation_rate:
                mutaded[i] += np.random.normal(0, 0.5) # Aplica uma pequena perturbação gaussiana
                mutaded[i] = np.clip(mutaded[i], self.min_value, self.max_value) # Garante que o novo valor continue dentro dos limites

        return mutaded
    
    def run(self) -> Tuple[np.ndarray, float, List[float]]:
        """
        Executa o algoritmo genético.
        """
        population = self.initialize_population()
        best_fitness_history = []
        average_fitness_history = []

        for generation in range(self.max_generations):
            # Fitness de cada individuo
            fitness = [self.evaluate_fitness(ind) for ind in population]
            average_fitness = np.mean(fitness)
            average_fitness_history.append(average_fitness)
            
            # Melhor fitness da atual geração
            current_best_fitness = min(fitness)
            best_fitness_history.append(current_best_fitness)

            # Critério de parada (se o fitness já está muito pequeno)
            #if current_best_fitness < 1e-6:
                #break

            # Nova população
            new_population = []

            # Elitismo: manter os melhores indíviduos de acordo com self.elitism_count
            elite_indices = np.argsort(fitness)[:self.elitism_count]
            new_population.extend([population[i] for i in elite_indices])
            
            # Preenche a nova população
            while len(new_population) < self.population_size:
                parent1 = self.tournament_selection(population, fitness)
                parent2 = self.tournament_selection(population, fitness)

                # Cruzamento
                if random.random() < self.crossover_rate:
                    child1, child2 = self.arithmetic_crossover(parent1, parent2)
                else:
                    child1, child2 = parent1.copy(), parent2.copy()
                
                # Mutação
                child1 = self.gaussian_mutation(child1)
                child2 = self.gaussian_mutation(child2)

                if len(new_population) < self.population_size:
                    new_population.append(child1)
                if len(new_population) < self.population_size:
                    new_population.append(child2)
            
            # Atualiza população para a próxima geração
            population = new_population
        
        fitness = [self.evaluate_fitness(ind) for ind in population]
        best_index = np.argmin(fitness)
        best_individual = population[best_index]
        best_fitness = fitness[best_index]

        return best_individual, best_fitness, best_fitness_history, average_fitness_history

def compare_solutions(params_variation: dict) -> List[dict]:
    """
    Compara a execução do algoritmo com diversos parâmetros.
    """
    results = []
    for name, params in params_variation.items():
        fitness_history = []
        generations_to_converge = []
        
        for _ in range(10):  # 10 execuções
            ga = GeneticAlgorithm(**params)
            _, best_fitness, history, _ = ga.run()
            fitness_history.append(best_fitness)
            generations_to_converge.append(len(history))
        
        results.append({
            'Configuração': name,
            'Tamanho_População': params['population_size'],
            'Taxa_Mutação': params['mutation_rate'],
            'Tamanho_Torneio': params['tournament_size'],
            'Fitness_Final': np.mean(fitness_history),
            'Gerações_Convergência': np.mean(generations_to_converge)
        })
    
    return results
    

ga = GeneticAlgorithm(population_size=10, mutation_rate=0.5,
                      tournament_size=3, crossover_rate=0.5,
                      elitism_count=2, max_generations=100)

populacao = ga.initialize_population()

best_solution, best_fitness, best_fitness_history, average_fitness_history = ga.run()
print(f"Melhor solução encontrada: {best_solution}")
print(f"Valor da função: {best_fitness}")

plt.plot(best_fitness_history, label="Melhor fitness")
plt.plot(average_fitness_history, label="Fitness Médio")
plt.title("Convergência do Algoritmo Genético")
plt.xlabel("Geração")
plt.ylabel("Melhor Fitness")
plt.legend()
plt.show()


# Variações a testar
param_variations = {
    'Padrão': {'population_size': 100, 'mutation_rate': 0.5, 'tournament_size': 3, 'crossover_rate': 0.2, 'elitism_count': 2, 'max_generations': 100},
    'Alta taxa de mut.': {'population_size': 100, 'mutation_rate': 0.9, 'tournament_size': 3, 'crossover_rate': 0.2, 'elitism_count': 2, 'max_generations': 100},
    'Baixa taxa de mut.': {'population_size': 100, 'mutation_rate': 0.1, 'tournament_size': 3, 'crossover_rate': 0.2, 'elitism_count': 2, 'max_generations': 100},
    'Pop. Pequena': {'population_size': 20, 'mutation_rate': 0.5, 'tournament_size': 3, 'crossover_rate': 0.2, 'elitism_count': 2, 'max_generations': 100},
    'Pop. Grande': {'population_size': 300, 'mutation_rate': 0.5, 'tournament_size': 3, 'crossover_rate': 0.2, 'elitism_count': 2, 'max_generations': 100},
}

results = compare_solutions(param_variations)
results = pd.DataFrame(results)
results.to_csv("results.csv")

