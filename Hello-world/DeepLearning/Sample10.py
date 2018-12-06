import keras
from keras import optimizers
from keras import losses
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import plot_model
import matplotlib.pyplot as plt
import numpy as np

INPUT_DATA = np.linspace(-1.0,1.0,100)
OUTPUT_DATA = np.sin(INPUT_DATA * np.pi)
EPOCH = 10

model = Sequential()
model.compile(loss='mean_absolute_error', optimizer="adam")
model.add(Dense(3,activation="sigmoid",input_shape=(1,)))
model.add(Dense(1,activation="linear"))
model.summary()

for j in range(1,EPOCH):
	plot_x = []
	plot_y = []

	for i in INPUT_DATA:
		output = model.predict(np.array([i]))
		plot_x.append(i)
		plot_y.append(output)

	model.fit(INPUT_DATA,OUTPUT_DATA,batch_size=len(INPUT_DATA),verbose=0,epochs=EPOCH * 300)

	plt.plot(INPUT_DATA,OUTPUT_DATA,linestyle="dashed")
	plt.scatter(plot_x,plot_y,marker="+")
	plt.show()

for i in INPUT_DATA:
	output = model.predict(np.array([i]))
	plot_x.append(i)
	plot_y.append(output)