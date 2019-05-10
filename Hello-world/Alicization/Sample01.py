
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import random
import sys
import tensorflow as tf
import itertools
import os
import neat
from neat import nn, population, statistics

from statistics import mean, median,variance,stdev

import alice as ac

env = ac.env()

def eval_fitness(genomes):
	for g in genomes:
		observation = env.reset()
		# env.render()
		net = nn.create_feed_forward_phenotype(g)
		fitness = 0
		reward = 0
		frames = 0
		total_fitness = 0

		for k in range(5):
			while 1:
				inputs = observation / 20.0

				# active neurons
				output = net.serial_activate(inputs)

				output = np.clip(output, -1, 1)
				# print(output)
				observation, reward, done, info = env.step(np.argmax(output))


				fitness += reward
				frames += 1
				# env.render()
				if done or frames > 1000:
					total_fitness += fitness
					# print(fitness)
					observation = env.reset()
					break
		# evaluate the fitness
		g.fitness = total_fitness / 5
	print(max([genomes[i].fitness for i in range(len(genomes))]))

def main(args):
	global plt
	local_dir = os.path.dirname(__file__)
	config_path = os.path.join(local_dir, "env01.config")

	pop = population.Population(config_path)
	pop.run(eval_fitness, 2000)
	winner = pop.statistics.best_genome()
	del pop

	winningnet = nn.create_feed_forward_phenotype(winner)

	streak = 0

	while streak < 100:
		fig = plt.figure()
		ims = []

		fitness,frames,reward = 0,0,0
		observation = env.reset()
		env.render()
		while 1:
			inputs = observation

			# active neurons
			output = winningnet.serial_activate(inputs)
			output = np.clip(output, -1, 1)
			# print(output)
			observation, reward, done, info = env.step(np.argmax(output))

			fitness += 1

			im = plt.imshow(env.render())
			ims.append([im])
			frames += 1

			if done or frames > 2000:
				print(fitness)
				print ('streak: ', streak)
				if fitness >= 170:
						streak += 1
				else:
					streak = 0

				break
		ani = animation.ArtistAnimation(fig, ims, interval=250)
		plt.show()

	print("completed!")

main(sys.argv)