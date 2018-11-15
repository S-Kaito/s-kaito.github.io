import numpy as np
import tensorflow as tf

from abc import ABCMeta , abstractmethod

WEIGHT = 0.01
ETA = 0.1

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
		print(this.y)
		this.y = np.exp(this.y)/np.sum(np.exp(this.y),axis=1,keepdims=True)

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
		this.map = [np.zeros((1,25)),np.zeros((1,25)),np.zeros((1,25)),np.zeros((1,25))]
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