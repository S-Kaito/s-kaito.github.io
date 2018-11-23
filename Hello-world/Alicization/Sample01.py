
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import tensorflow as tf

from statistics import mean, median,variance,stdev

import alice as ac

EPOCH = 10000

def run(creat):

	MAP = np.random.randint(-19,20,(100,100))
	ANS = np.sum(MAP[MAP > 0])

	x = 50
	y = 50
	point = 0

	plot_x = []
	plot_y = []
	death = []
	error = [0]
	deathCount = 0

	for j in range(1,EPOCH):
		creat.forward(np.array(MAP[x - 2:x + 3,y - 2:y + 3]).reshape(1,25))

		creat.memory(map=np.array(MAP[x - 2:x + 3,y - 2:y + 3]).reshape(1,25),action=np.random.choice([0,1,2,3], 1, p=np.exp(creat.network.y.reshape(-1))/np.sum(np.exp(creat.network.y.reshape(-1))).reshape(-1)))
		#creat.memory(map=np.array(MAP[x - 2:x + 3,y - 2:y + 3]).reshape(1,25),action=np.argmax(creat.network.y))
		
		if creat.action[-1][0] == 0:
			y -= 1
		elif creat.action[-1][0] == 1:
			y += 1
		elif creat.action[-1][0] == 2:
			x += 1
		elif creat.action[-1][0] == 3:
			x -= 1

		point += MAP[x][y]

		error[-1] += (ac.clipping(MAP[x][y]) - ac.clipping(creat.network.y[0][creat.action[-1][0]])) ** 2

		creat.memory(point=MAP[x][y])

		MAP[x][y] = 0

		if (x == 9 or x == 90) or (y == 9 or y == 90):
			x = 50
			y = 50
			deathCount += 1
			
		if j % (EPOCH / 100) == 0:

			error[-1] *= 10

			plot_x.append(j)
			plot_y.append(point)
			death.append(deathCount * 100)
			error.append(0)

		if j % (EPOCH / 20) == 0:
			print()
			print(j," / ",EPOCH,"  POINT:",point,"/",ANS," DEATH:",deathCount)
			print(np.array(MAP[x - 3:x + 4,y - 3:y + 4]))
			
		MAP[0:10,:] = -20
		MAP[-10:,:] = -20
		MAP[:,0:10] = -20
		MAP[:,-10:] = -20
		MAP[MAP > 20] = 20

	print(np.sum(MAP[MAP > 0]),"/",ANS)
	print(MAP[10:-10,10:-10])
	plt.cla()
	plt.scatter(plot_x,plot_y,marker="+")
	plt.scatter(plot_x,death,marker="*")
	plt.scatter(plot_x,error[0:-1],marker="o")
	
	creat.learn()

	return plt,(plot_y[-1],death[-1],mean(error))

def main(args):
	N = 1 if ("-t" not in args) else int(args[int(args.index('-t')) + 1])
	plot_x= []
	point = []
	death = []
	error = []
	for i in range(N):
		creat = ac.Creat(ac.Network([ac.LayerSigmoid(25,100),ac.LayerSigmoid(100,100),ac.LayerSigmoid(100,50),ac.LayerIdentity(50,4)]))
		if "-r" in args:
			creat.load()
		
		plt,result = run(creat)
		plot_x.append(i + 1)
		point.append(result[0])
		death.append(result[1])
		error.append(result[2])
		if "-show-all" in args or i == N - 1:
			plt.show()

		if "-w" in args:
			creat.save()

	plt.cla()
	plt.scatter(plot_x,point,marker="+")
	plt.scatter(plot_x,death,marker="*")
	plt.scatter(plot_x,error,marker="o")
	plt.title("Total Result")
	plt.xlabel("Times")
	plt.show()

main(sys.argv)