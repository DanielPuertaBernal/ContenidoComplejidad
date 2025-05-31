import pygame
import random
import sys
"""
Introducción al Problema de las 8 Reinas (Algoritmo Genético)

Descripción del Problema:
El problema de las Ocho Reinas es un desafío clásico de ajedrez y de lógica que consiste en colocar
ocho reinas en un tablero de ajedrez estándar de 8x8 de tal manera que ninguna reina ataque a otra.
Esto significa que no debe haber dos reinas en la misma fila, en la misma columna o en la misma diagonal.

Enfoque de Solución (Algoritmo Genético):
Resolver este problema "a mano" o por fuerza bruta puede ser computacionalmente costoso. En lugar de ello,
emplearemos un algoritmo genético, una metaheurística inspirada en la evolución biológica. Este enfoque implica:

1.  Representación: Cada posible disposición de las 8 reinas se representa como un "individuo" (un cromosoma),
    donde cada posición indica la columna de una reina en una fila específica.
2.  Población Inicial: Se genera un conjunto de soluciones aleatorias (la primera generación).
3.  Función de Fitness: Se evalúa qué tan "buena" es cada solución calculando el número de pares de reinas
    que se atacan entre sí. Un "fitness" de 0 significa que no hay ataques y se ha encontrado una solución válida.
4.  Selección y Reproducción: Las soluciones con mejor fitness tienen una mayor probabilidad de ser seleccionadas
    para "reproducirse", creando nuevas soluciones (descendencia) a través de la combinación de sus características
    (cruce) y pequeñas modificaciones aleatorias (mutación).
5.  Evolución: Este proceso se repite a lo largo de "generaciones" hasta que se encuentra una solución óptima
    (fitness de 0) o se alcanza un criterio de parada.
"""

# Inicializar Pygame
pygame.init()

# Configuración de ventana
size = width, height = 480, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("8 Reinas")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
QUEEN_COLOR = (255, 0, 0)

# Cargar imagen de reina o dibujar una simple
queen = pygame.Surface((50, 50))
pygame.draw.circle(queen, QUEEN_COLOR, (25, 25), 20)

def draw_board(solution):
    block_size = width // 8
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * block_size, row * block_size, block_size, block_size))
            if solution[row] == col:
                screen.blit(queen, (col * block_size + 5, row * block_size + 5))

def main(solution):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_board(solution)
        pygame.display.flip()

import random

# Cada individuo es una lista de 8 números (columna de cada reina en cada fila)
def create_individual():
    return [random.randint(0, 7) for _ in range(8)]

def fitness(individual):
    attacks = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            # Dos reinas atacan si están en la misma columna o diagonal
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                attacks += 1
    return attacks

def crossover(parent1, parent2):
    cut = random.randint(1, 7)
    return parent1[:cut] + parent2[cut:]

def mutate(individual):
    idx = random.randint(0, 7)
    individual[idx] = random.randint(0, 7)

def genetic_algorithm():
    population = [create_individual() for _ in range(100)]
    generation = 0

    while True:
        population.sort(key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            return population[0]

        next_generation = population[:20]  # Elitismo: conservamos los mejores

        # Reproducir
        while len(next_generation) < 100:
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = crossover(parent1, parent2)
            if random.random() < 0.3:  # 30% de mutación
                mutate(child)
            next_generation.append(child)

        population = next_generation
        generation += 1
        if generation % 10 == 0:
            print(f"Generación {generation} - Mejor fitness: {fitness(population[0])}")

if __name__ == "__main__":
    sol = genetic_algorithm()
    print("Solución encontrada:", sol)
    main(sol)