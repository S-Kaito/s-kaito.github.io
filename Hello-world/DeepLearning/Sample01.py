%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

INPUT_DATA = (np.arange(0,np.pi*2,0.1)-np.pi)/np.pi
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

layer.w = np.array([[ 1.5226207,-4.74313941,-5.09765436]])
layer.b = np.array([ 0.05025657,0.25530377,-1.12453411])

output.w = np.array([9.01367277,5.04463465,1.2634446 ])
output.b = np.array([-7.73053153])

plot_x = []
plot_y = []

for i in INPUT_DATA:
    layer.forward(np.array([i]).reshape(1,1))
    output.forward(layer.y)
    
    plot_x.append(i)
    plot_y.append(output.y)

plt.scatter(plot_x,plot_y,marker="+")
plt.show()