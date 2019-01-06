import random

# constants
POP_SIZE = 6
GENOME_SIZE = 5
GENERATIONS = 10
PROB_MUTATION = 0.1
TOURAMENT_SIZE = 3

# functions
def population_initialise():
    return([(''.join(random.choice("01") for i in range(GENOME_SIZE))) 
                        for i in range(POP_SIZE)])

def fitness(chromosome):
    return str(chromosome).count("1")

def selection(population):
    tournament = [random.choice(population) for i in range(TOURAMENT_SIZE)]
    fitnesses = [fitness(tournament[i] for i in range(TOURAMENT_SIZE))]
    return tournament[fitnesses.index(max(fitnesses))]

def crossing_over(parent1, parent2):
    parent1, parent2 = str(parent1), str(parent2)
    xo_point = random.randint(1, GENOME_SIZE-1)
    return([
            parent1[0:xo_point] + parent2[xo_point:GENOME_SIZE],
            parent2[0:xo_point] + parent1[xo_point:GENOME_SIZE] ])

def mutate_mech(bit):
    bit = str(bit)
    if bit == "0":
        return "1"
    else:
        return "0"

def mutation(chromosome):
    chromosome = str(chromosome)
    for i in range(GENOME_SIZE):
        if random.random() < PROB_MUTATION:
            chromosome = chromosome[:i] + mutate_mech(i) + chromosome[i+1:]
    return(chromosome)

def print_population(population):            
    fitnesses = [fitness(population[i]) for i in range(POP_SIZE)]
    print(list(zip(population, fitnesses)))
    
# Algorithm
random.seed()
population = population_initialise()

for gen in range(GENERATIONS):
    print("Genneration " + str(gen))
    print_population(population)
    if max([fitness(population[i]) for i in range(POP_SIZE)]) == GENOME_SIZE:
        break;
    nextgen_population = []
    for i in range(int(POP_SIZE/2)):
        parent1 = selection(population)
        parent2 = selection(population)
        offspring = crossing_over(parent1, parent2)
        nextgen_population.append(mutation(offspring[0]))
        nextgen_population.append(mutation(offspring[1]))
    population = nextgen_population
    