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
		self.genom = []
		self.array = np.random.shuffle(POINT_NUMBER)
		a = np.arange(range(POINT_NUMBER))
		for i in range(POINT_NUMBER):
			self.genom.append(np.where(a == self.array[i]))
			a.remove(self.genom[i])

	def getGenom(self):
		return self.genom

	def getArray(self):
		return self.array

	def getEvaluation(self):
		return 0


for i in range(POINT_NUMBER):
	ROOT_X.append(np.randint(MAX_X))
	ROOT_Y.append(np.randint(MAX_Y))

ind = Indivisual()
print ind.getGenom()


