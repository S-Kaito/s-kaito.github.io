
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import tensorflow as tf

import alice as ac

EPOCH = 100

def run(creat):

	MAP = np.random.randint(-19,20,(100,100))
	ANS = np.sum(MAP)

	x = 50
	y = 50
	point = 0
	plot_x = []
	plot_y = []
	death = []
	deathCount = 0

	for j in range(EPOCH):
		creat.forward(np.array(MAP[x - 2:x + 3,y - 2:y + 3]).reshape(1,25)/20)

		creat.memory(np.array(MAP[x - 2:x + 3,y - 2:y + 3]).reshape(1,25)/20,np.random.choice(np.array([0,1,2,3]), 1, p=np.exp(creat.evaluation)/np.sum(np.exp(creat.evaluation)).reshape(-1)))

		
		if creat.action[-1] == 0:
			y -= 1
		elif creat.action[-1] == 1:
			y += 1
		elif creat.action[-1] == 2:
			x += 1
		elif creat.action[-1] == 3:
			x -= 1
		point += MAP[x][y]

		if j > 5:
			creat.learn(MAP[x][y]/20)
		MAP[x][y] = 0

		if (x == 8 or x == 91) or (y == 8 or y == 91):
			creat.learn(MAP[x][y]/20)
			x = 50
			y = 50
			deathCount += 1
			
		if j % (EPOCH / 100) == 0:
			plot_x.append(j)
			plot_y.append(point)
			death.append(deathCount * 100)
		if j % (EPOCH / 20) == 0:
			print()
			print(j," / ",EPOCH,"  POINT:",point,"/",ANS," DEATH:",deathCount)
			print(np.array(MAP[x - 3:x + 4,y - 3:y + 4]))
			#print(creat.brain[-1].y,np.argmax(creat.brain[-1].y))
			
		MAP[0:10,:] = -20
		MAP[-10:,:] = -20
		MAP[:,0:10] = -20
		MAP[:,-10:] = -20
		MAP[MAP > 20] = 20

	print(np.sum(MAP),"/",ANS)
	print(MAP)
	plt.scatter(plot_x,plot_y,marker="+")
	plt.scatter(plot_x,death,marker="*")
	plt.show()

def main(args):
	creat = ac.Creat(ac.Network([ac.LayerSigmoid(29,100),ac.LayerSigmoid(100,100),ac.LayerSigmoid(100,100),ac.LayerIdentity(100,1)]))
	if "-r" in args:
		creat.load()
	
	run(creat)

	if "-w" in args:
		creat.save()

main(sys.argv)