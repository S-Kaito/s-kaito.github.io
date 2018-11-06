
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

WEIGHT = 0.1
EPOCH = 2000
MAP = np.random.randint(0,100,(110,110))
MAP[0:99][0] = 0
MAP[0:99][98]= 0
MAP[0][0:99] = 0
MAP[99][0:99]= 0

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

brain = []
brain.append(MiddleLayer(25,10))
brain.append(MiddleLayer(10,10))
brain.append(MiddleLayer(10,10))
brain.append(MiddleLayer(10,10))
brain.append(Layer(10,5))

x = 50
y = 50
point = 0
action = []
plot_x = []
plot_y = []
for j in range(EPOCH):
    print(np.array(MAP[x - 2::x + 2][y - 2::y + 2]).shape)
    brain[0].forward(np.array(MAP[x - 2:x + 2][y - 2:y + 2]).reshape(1,-1))
    for i in range(1,5):
        brain[i].forward(brain[i - 1].y)
    action.append(np.where(brain[4].y == np.amax(brain[4].y)))
    if action == 0:
        y -= 1
    elif action == 1:
        y += 1
    elif action == 2:
        x += 1
    elif action == 3:
        x -= 1
    elif action == 4:
        point += MAP[x][y]
        brain[4].backward([[0,0,0,0,MAP[x][y] / 10]])
        for i in range(3,-1,-1):
            brain[i].backword(brain[i - 1].grad_x)

        for i in brain:
            i.update()

    if j % (EPOCH / 20) == 0:
        print(j + (EPOCH / 20)," / ",EPOCH)
        plot_x.append(j)
        plot_y.append(point)

plt.scatter(plot_x,plot_y,marker="+")
plt.show()