# tsp_utils.py

import tsplib95
import random

def load_tsp_data(file_path):
    problem = tsplib95.load(file_path)
    return problem

def initialize_population(population_size, num_cities):
    return [random.sample(range(1, num_cities + 1), num_cities) for _ in range(population_size)]

def calculate_total_distance(solution, problem):
    distance = 0
    for i in range(len(solution) - 1):
        distance += problem.get_weight(solution[i], solution[i + 1])
    distance += problem.get_weight(solution[-1], solution[0])
    return distance
