
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

INPUT_DATA = np.linspace(-1.0,1.0,100)
OUTPUT_DATA = np.cos(INPUT_DATA * np.pi)
WEIGHT = 0.1
EPOCH = 2000

class Layer:
    def __init__(this,input_num,output_num):
        this.w = WEIGHT * np.random.randn(input_num,output_num)
        this.b = WEIGHT * np.random.randn(output_num)
        
    def forward(this,x):
        this.x = x
        this.y = np.dot(x,this.w) + this.b

    def backward(this,x):
        delta = this.y - x

        this.grad_w = np.dot(this.x.T,delta)
        this.grad_b = np.sum(delta,axis=0)

        this.grad_x = np.dot(delta,this.w.T)

    def update(this):
        this.w -= this.grad_w * WEIGHT
        this.b -= this.grad_b * WEIGHT

class MiddleLayer(Layer):
    def forward(this,x):
        super().forward(x)
        this.y = 1/(1+(np.exp(-this.y)))

    def backward(this,x):  
        delta = x * (1 - this.y) * this.y

        this.grad_w = np.dot(this.x.T,delta)
        this.grad_b = np.sum(delta,axis=0)

        this.grad_x = np.dot(delta,this.w.T)

layer = MiddleLayer(1,3)
output = Layer(3,1)

fig = plt.figure()

img = []
    
for j in range(EPOCH):
    plot_x = []
    plot_y = []
    for i in INPUT_DATA:
        layer.forward(np.array([i]).reshape(1,1))
        output.forward(layer.y)

        plot_x.append(i)
        plot_y.append(np.sum(output.y))

        output.backward(OUTPUT_DATA[np.where(INPUT_DATA == i)].reshape(1,1))
        layer.backward(output.grad_x)

        layer.update()
        output.update()

    if j % (EPOCH / 20) == 0:
        print(j + (EPOCH / 20)," / ",EPOCH)
        print(layer.w,layer.b)
        print(output.w,output.b)
        plt.plot(INPUT_DATA,OUTPUT_DATA,linestyle="dashed")
        line = plt.scatter(plot_x,plot_y,marker="+")
        img.append(line)
ani = animation.ArtistAnimation(fig,img)
plt.show()