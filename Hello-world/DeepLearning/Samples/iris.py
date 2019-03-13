from sklearn import datasets
import keras
from keras import optimizers
from keras import losses
from keras.models import Sequential
from keras.models import model_from_config
from keras.models import model_from_json
from keras.layers import Dense
from keras.optimizers import RMSprop
from keras.utils import plot_model
from keras import backend as K

import matplotlib.pyplot as plt 
import numpy as np


iris = datasets.load_iris()
model = Sequential()
model.add(Dense(16,activation="relu",input_dim=4))
model.add(Dense(16,activation="relu"))
model.add(Dense(4,activation="softmax"))
model.summary()

data = iris.data[:,:]
target = iris.target[:]

x = []
y = []

for i in range(25):
	data_test = np.random.choice(range(0,len(data)),size=100)
	x.append(i)
	y.append(0)
	print(data[0])
	for j in data_test:
		out = model.predict(data[j])
		if np.argmax(out) == y:
			y[-1] += 1
	model.fit(np.array(data),np.array(target),batch_size=64,verbose=0,epochs=1)
	print(i,":",x/100)
plt.scatter(x,y,marker="+")
plt.show()
