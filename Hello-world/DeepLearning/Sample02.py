
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

INPUT_DATA = np.linspace(-1.0,1.0,100)
OUTPUT_DATA = np.sin(INPUT_DATA)
WEIGHT = 0.1

class Layer:
    def __init__(this,input_num,output_num):
        this.w = WEIGHT * np.random.randn(input_num,output_num)
        this.b = WEIGHT * np.random.randn(output_num)
        
    def forward(this,x):
        this.x = x
        this.y = np.dot(x,this.w) + this.b

    def backward(this,x):
        this.bx = x
        this.by = np.dot(x,this.w.T)

    def update(this):
        this.w -= (this.w - this.by.T) * WEIGHT
        this.b -= (np.sum(this.y) - np.sum(this.by)) * WEIGHT

class MiddleLayer(Layer):
    def forward(this,x):
        super().forward(x)
        this.y = 1/(1+(np.exp(-this.y)))

layer = MiddleLayer(1,3)
output = Layer(3,1)

fig = plt.figure()
img = []

for j in range(100):
    plot_x = []
    plot_y = []
    for i in INPUT_DATA:
        layer.forward(np.array([i]).reshape(1,1))
        output.forward(layer.y)

        plot_x.append(i)
        plot_y.append(np.sum(output.y))

        output.backward(OUTPUT_DATA[np.where(INPUT_DATA == i)].reshape(1,1))
        layer.backward(output.by)

        layer.update()
        output.update()

    if j % 10 == 0:
        print(j," / 100 ",layer.w,layer.b,output.w,output.b)
    plt.plot(INPUT_DATA,OUTPUT_DATA,linestyle="dashed")
    line, = plt.plot(plot_x,plot_y,"r")
    img.append([line])
ani = animation.ArtistAnimation(fig,img)
plt.show()