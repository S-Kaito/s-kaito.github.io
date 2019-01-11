import copy
from deap import base
from deap import creator
from deap import tools
import numpy as np
import random
import string
import sys
import time

EPOCH = 1000

def action(ind):
	s = "Hello,world!"
	error = 0
	for i in range(0,11):
		if s[i] != ind[i]:
			error += 1
	return error,

def init():
	return ''.join(random.choices(string.ascii_letters + string.punctuation, k=1))

def mutate(ind,indpb=0.1):
	for c in ind:
		if random.random() < indpb:
			c = random.choices(string.ascii_letters + string.digits, k=1)
	
def main(args):
	creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
	creator.create("Individual", list, fitness=creator.FitnessMax)

	toolbox = base.Toolbox()

	toolbox.register("attr_bool", init)
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool,len('Hello,world!'))
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)

	toolbox.register("evaluate", action)
	toolbox.register("mate", tools.cxUniform,50)
	toolbox.register("mutate", mutate, indpb=0.1)
	toolbox.register("select", tools.selTournament, tournsize=3)

	pop = toolbox.population(n=99)
	CXPB, MUTPB, NGEN = 0.5, 0.2, 40

	fitnesses = list(map(toolbox.evaluate, pop))
	for ind, fit in zip(pop, fitnesses):
		ind.fitness.values = fit

	print("Start of evolution")

	for episode in range(EPOCH):

		offspring = list(map(toolbox.clone, toolbox.select(pop, len(pop))))

		for child1, child2 in zip(offspring[::2], offspring[1::2]):

			if random.random() < CXPB:
				toolbox.mate(child1, child2)
				del child1.fitness.values
				del child2.fitness.values

		for mutant in offspring:

			if random.random() < MUTPB:
				toolbox.mutate(mutant)
				del mutant.fitness.values
	
		invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
		fitnesses = map(toolbox.evaluate, invalid_ind)
		for ind, fit in zip(invalid_ind, fitnesses):
			ind.fitness.values = fit
		
		pop[:] = offspring
		
		fits = [ind.fitness.values for ind in pop]
		
		print(episode,"|",''.join(tools.selBest(pop, 1)[0]))

	print("-- End of (successful) evolution --")
	
	best_ind = tools.selBest(pop, 1)[0]
	print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))

main(sys.argv)