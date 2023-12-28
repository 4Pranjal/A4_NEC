# genetic_algorithm.py

import random
import numpy as np
from tsp_utils import initialize_population, calculate_total_distance

def tournament_selection(population, k, problem):
    selected_parents = []
    for _ in range(len(population)):
        tournament = random.sample(population, k)
        best_solution = min(tournament, key=lambda x: calculate_total_distance(x, problem))
        selected_parents.append(best_solution)
    return selected_parents

def roulette_wheel_selection(population, problem):
    fitness_values = [1 / calculate_total_distance(solution, problem) for solution in population]
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    selected_parents = np.random.choice(population, size=len(population), p=probabilities, replace=True)
    return selected_parents

def order_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child1 = parent1[start:end] + [city for city in parent2 if city not in parent1[start:end]]
    child2 = parent2[start:end] + [city for city in parent1 if city not in parent2[start:end]]
    return child1 + child2[start:] + child2[:start], child2 + child1[start:] + child1[:start]

def partially_matched_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    mapping1 = {parent1[i]: parent2[i] for i in range(start, end)}
    mapping2 = {parent2[i]: parent1[i] for i in range(start, end)}
    child1 = [mapping1.get(city, city) for city in parent1]
    child2 = [mapping2.get(city, city) for city in parent2]
    return child1, child2

def swap_mutation(solution):
    idx1, idx2 = random.sample(range(len(solution)), 2)
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

def inversion_mutation(solution):
    start, end = sorted(random.sample(range(len(solution)), 2))
    solution[start:end] = reversed(solution[start:end])
    return solution
