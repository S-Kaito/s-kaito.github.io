
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import tensorflow as tf

from abc import ABCMeta , abstractmethod

WEIGHT = 0.01
ETA = 0.1
EPOCH = 10000

class Layer(metaclass=ABCMeta):
	def __init__(this,input_num,output_num):
	   this.w = WEIGHT * np.random.randn(input_num,output_num)
	   this.b = WEIGHT * np.random.randn(output_num)

	@abstractmethod
	def forward(this,x):
		pass

	@abstractmethod
	def backward(this,x):
		pass

	def update(this):
		this.w -= this.grad_w * ETA
		this.b -= this.grad_b * ETA

class LayerIdentity(Layer):
	def forward(this,x):
		this.x = x
		this.y = np.dot(x,this.w) + this.b

	def backward(this,x):
		delta = this.y - x

		this.grad_w = np.dot(this.x.T,delta)
		this.grad_b = np.sum(delta,axis=0)

		this.grad_x = np.dot(delta,this.w.T)

class LayerLeakyReLU(Layer):
	def forward(this,x):
		this.x = x
		this.y = np.dot(x,this.w) + this.b
		this.y = np.where(this.y <= 0,0.01 * this.y,this.y)

	def backward(this,x):
		delta = np.where(this.y <= 0,0.01,1)

		this.grad_w = np.dot(this.x.T,delta)
		this.grad_b = np.sum(delta,axis=0)

		this.grad_x = np.dot(delta,this.w.T)

class LayerSigmoid(Layer):
	def forward(this,x):
		this.x = x
		this.y = np.dot(x,this.w) + this.b
		this.y = 1/(1+(np.exp(-this.y)))

	def backward(this,x):  
		delta = x * (1 - this.y) * this.y

		this.grad_w = np.dot(this.x.T,delta)
		this.grad_b = np.sum(delta,axis=0)

		this.grad_x = np.dot(delta,this.w.T)

class LayerSoftmax(Layer):
	def forward(this,x):
		this.x = x
		this.y = np.dot(x,this.w) + this.b
		this.y = np.exp(this.y)/(np.sum(np.exp(this.y),axis=1,keepdims=True) + 1)

	def backward(this,x):  
		delta = this.y - x

		this.grad_w = np.dot(this.x.T,delta)
		this.grad_b = np.sum(delta,axis=0)

		this.grad_x = np.dot(delta,this.w.T)

class DropoutLayer(Layer):
	def __init__(this,p=0.5):
		this.p = p

	def forward(this,x):
		rand = np.random.rand(*x.shape)
		this.dropout = np.where(rand > this.p , 1 , 0)
		this.y = x * this.dropout

	def backward(this,grad_y):
		this.grad_x = grad_y * this.dropout

	def update(this):
		()

class Creat:
	def __init__(this,brain):
		this.brain = brain
		this.map = [np.zeros((1,49)),np.zeros((1,49)),np.zeros((1,49)),np.zeros((1,49))]
		this.action = [0,1,2,3]

	def forward(this,x):
		this.brain[0].forward(x)
		for i in range(1,len(this.brain)):
			this.brain[i].forward(this.brain[i - 1].y)
		return this.brain[-1].y

	def backward(this,x):
		this.brain[-1].backward(x)
		for i in range(len(this.brain) - 2,-1,-1):
			this.brain[i].backward(this.brain[i + 1].grad_x)

	def update(this):
		for i in this.brain:
			i.update()

	def memory(this,map,action):
		this.map.append(map)
		this.action.append(action)

	def learn(this,point):
		for i in range(1,4):
			a = np.zeros(4)
			a[this.action[-i]] += point / ((i))
			this.forward(this.map[-i])
			this.backward(a)
			this.update()

	def save(this):
		for i in range(0,len(this.brain)):
			np.savetxt('w0' + str(i) + '.csv', this.brain[i].w, delimiter=',')
			np.savetxt('b0' + str(i) + '.csv', this.brain[i].b, delimiter=',')

	def load(this):
		for i in range(0,len(this.brain)):
			this.brain[i].w = np.loadtxt('w0' + str(i) + '.csv', delimiter=',')
			this.brain[i].b = np.loadtxt('b0' + str(i) + '.csv', delimiter=',')

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
		creat.forward(np.array(MAP[x - 3:x + 4,y - 3:y + 4]).reshape(1,49)/20)
		creat.memory(np.array(MAP[x - 3:x + 4,y - 3:y + 4]).reshape(1,49)/20,np.random.choice(np.array([0,1,2,3]), 1, p= (np.exp(creat.brain[-1].y)/np.sum(np.exp(creat.brain[-1].y))).reshape(-1)))

		
		if creat.action[-1] == 0:
			y -= 1
		elif creat.action[-1] == 1:
			y += 1
		elif creat.action[-1] == 2:
			x += 1
		elif creat.action[-1] == 3:
			x -= 1
		point += MAP[x][y]
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
	creat = Creat([LayerLeakyReLU(49,100),LayerLeakyReLU(100,100),LayerLeakyReLU(100,100),LayerSoftmax(100,4)])
	if "-r" in args:
		creat.load()
	
	run(creat)

	if "-w" in args:
		creat.save()

main(sys.argv)