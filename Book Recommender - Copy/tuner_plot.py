import matplotlib.pyplot as plt
import csv
import pandas as pd

def read_excel(filename):
    df = pd.read_excel(filename)
    pop_size_list = df['pop_size'].tolist()
    mutation_rate_list = df['mutation_rate'].tolist()
    num_generations_list = df['num_generations'].tolist()
    crossover_func_list = df['crossover_func'].tolist()
    mutation_func_list = df['mutation_func'].tolist()
    no_rec_list = df['no_rec'].tolist()
    best_solution_list = df['best_solution'].tolist()
    semratings_dict_list = df['semratings_dict'].tolist()
    fitness_scores_dict_list = df['fitness_scores_dict'].tolist()
    best_solutions_by_generation_list = df['best_solutions_by_generation'].tolist()

    return pop_size_list, mutation_rate_list, num_generations_list, crossover_func_list, mutation_func_list, no_rec_list, best_solution_list, semratings_dict_list, fitness_scores_dict_list, best_solutions_by_generation_list

def plot_mutation_rate_vs_avg_fitness(mutation_rate_list, average_fitness_scores):
    plt.figure(figsize=(8, 6))
    plt.plot(mutation_rate_list, average_fitness_scores, marker='o', linestyle='-')
    plt.xlabel('Mutation Rate')
    plt.ylabel('Average Predicted Rating')
    plt.title('Average Predicted Rating for Mutation Rate')
    plt.grid(True)
    plt.savefig('mutation_rate_vs_avg_fitness.png')
    plt.show()

def plot_num_generations_vs_avg_fitness(num_generations_list, average_fitness_scores):
    plt.figure(figsize=(8, 6))
    plt.plot(num_generations_list, average_fitness_scores, marker='o', linestyle='-')
    plt.xlabel('Number of Generations')
    plt.ylabel('Average Predicted Rating')
    plt.title('Average Predicted Rating for Number of Generations')
    plt.grid(True)
    plt.savefig('num_generations_vs_avg_fitness.png')
    plt.show()

def plot_no_rec_vs_avg_fitness(no_rec_list, average_fitness_scores):
    plt.figure(figsize=(8, 6))
    plt.plot(no_rec_list, average_fitness_scores, marker='o', linestyle='-')
    plt.xlabel('Number of Recombinations')
    plt.ylabel('Average Predicted Rating')
    plt.title('Average Predicted Rating for Number of Recombinations')
    plt.grid(True)
    plt.savefig('no_rec_vs_avg_fitness.png')
    plt.show()

def plot_best_semrating_vs_semrating_of_best_solution(semratings_dict):
    best_semrating = max(semratings_dict.values())
    best_solution = max(semratings_dict, key=semratings_dict.get)

    plt.figure(figsize=(8, 6))
    plt.scatter(best_semrating, semratings_dict[best_solution], marker='o', color='blue', label='Best Solution')
    plt.axhline(y=best_semrating, linestyle='--', color='gray', label='Best Semrating')
    plt.axvline(x=semratings_dict[best_solution], linestyle='--', color='gray')
    plt.xlabel('Semrating')
    plt.ylabel('Best Solution Semrating')
    plt.title('Best Semrating vs Semrating of Best Solution')
    plt.legend()
    plt.grid(True)
    plt.savefig('best_semrating_vs_semrating_of_best_solution.png')
    plt.show()

def plot_average_ratings_by_pop_size(pop_size_list,best_solution_list, fitness_scores_dict):
    average_fitness_scores = [
        fitness_scores_dict[solution]["total_predicted_rating"]/len(solution)
        for solution in best_solution_list
    ]
    plt.figure(figsize=(8, 6))
    plt.plot(pop_size_list, average_fitness_scores, marker='o', linestyle='-')
    plt.xlabel('Population Size')
    plt.ylabel('Average Predicted Rating')
    plt.title('Average Predicted Rating for Population Size')
    plt.grid(True)
    plt.savefig('fitness_graph.png')
    plt.show()

def plot_comparison_systems(best_solutions_by_generation_dict, fitness_scores_dict_list):
    num_systems = len(best_solutions_by_generation_dict)

    fig, axes = plt.subplots(nrows=num_systems, ncols=2, figsize=(12, 5*num_systems))
    fig.subplots_adjust(hspace=0.5)

    for i, (fitness_scores_dict, best_solutions) in enumerate(zip(fitness_scores_dict_list, best_solutions_by_generation_dict.values())):
        generations = list(best_solutions_by_generation_dict.keys())
        fitness_scores = [fitness_scores_dict[solution]['total_predicted_rating'] for solution in best_solutions]

        # Plot best solutions by generations
        axes[i, 0].plot(generations, best_solutions, marker='o', linestyle='-')
        axes[i, 0].set_xlabel('Generation')
        axes[i, 0].set_ylabel('Best Solution Predicted Rating')
        axes[i, 0].set_title(f'System {i+1}: Best Solution by Generation')
        axes[i, 0].grid(True)

        # Plot fitness scores by generations
        axes[i, 1].plot(generations, fitness_scores, marker='o', linestyle='-')
        axes[i, 1].set_xlabel('Generation')
        axes[i, 1].set_ylabel('Total Predicted Rating')
        axes[i, 1].set_title(f'System {i+1}: Fitness Score by Generation')
        axes[i, 1].grid(True)

    plt.savefig('comparison_graph.png')
    plt.show()