import numpy as np
import matplotlib.pyplot as plt

INPUT_DATA = np.linspace(-1.0,1.0,100)
WEIGHT = 0.1

class Layer:
    def __init__(this,input_num,output_num):
        this.w = WEIGHT * np.random.randn(input_num,output_num)
        this.b = WEIGHT * np.random.randn(output_num)
        
    def forward(this,x):
        this.y = np.dot(x,this.w) + this.b

class MiddleLayer(Layer):
    def forward(this,x):
        super().forward(x)
        this.y = 1/(1+(np.exp(-this.y)))

layer = MiddleLayer(1,3)
output = Layer(3,1)

layer.w = np.array([[ 5,2,-5]])
layer.b = np.array([ 0.1,0.2,-1])

output.w = np.array([9,3,4])
output.b = np.array([-5])

plot_x = []
plot_y = []

for i in INPUT_DATA:
    layer.forward(np.array([i]).reshape(1,1))
    output.forward(layer.y)

    plot_x.append(i)
    plot_y.append(output.y)

plt.scatter(plot_x, plot_y, marker="+")
plt.show()