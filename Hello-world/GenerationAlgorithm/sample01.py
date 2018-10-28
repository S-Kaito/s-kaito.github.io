import numpy as np

POINT_NUMBER = 50
MAX_X = 100
MAX_Y = 100
ROOT_X = []
ROOT_Y = []

POPURATION = 100

MUTATION_RATE = 1/100

class Indivisual:
	def __init__(self):
		self.genom = np.array([])
		self.array = np.random.permutation(POINT_NUMBER)
		a = np.arange(POINT_NUMBER)
		for i in self.array:
			print(np.where(a==i))
			np.append(self.genom,np.where(a == i))
			np.delete(a,self.array[i])

	def getGenom(self):
		return self.genom

	def getArray(self):
		return self.array

	def getEvaluation(self):
		return 0


for i in range(POINT_NUMBER):
	ROOT_X.append(np.random.randint(MAX_X))
	ROOT_Y.append(np.random.randint(MAX_Y))

ind = Indivisual()
print(ind.getGenom())


