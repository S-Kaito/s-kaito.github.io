
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

WEIGHT = 0.1
EPOCH = 1000
MAP = np.random.randint(0,100,(100,100))
ANS = np.sum(MAP)
MAP[0:5,0:99] = -5
MAP[95:99,0:99] = -5
MAP[0:99,0:5] = -5
MAP[0:99,95:99] = -5

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
action = [0,1,2,3,4]
memory = [np.zeros(25) * 5]
plot_x = []
plot_y = []
for j in range(EPOCH):
    memory.append(np.array(MAP[x - 2:x + 3,y - 2:y + 3]).reshape(1,25))
    brain[0].forward(np.array(MAP[x - 2:x + 3,y - 2:y + 3]).reshape(1,25))
    for i in range(1,5):
        brain[i].forward(brain[i - 1].y)
    action.append(np.argmax(brain[4].y))

    args = np.zeros(5)
    a = np.zeros(5)
    if action[-1] == 0:
        y -= 1
    elif action[-1] == 1:
        y += 1
    elif action[-1] == 2:
        x += 1
    elif action[-1] == 3:
        x -= 1
    else:
        point += MAP[x][y]
        args[4] += MAP[x][y] / 10
        a[action[-2]] += MAP[x][y] / 15
        MAP[x][y] = 0

    args[action[-1]] -= 0.5
    
    brain[4].backward(args)
    for i in range(3,-1,-1):
        brain[i].backward(brain[i + 1].grad_x)
    for i in brain:
        i.update()
    
    print(args,a)

    brain[0].forward(memory[-2])
    for i in range(1,5):
        brain[i].forward(brain[i - 1].y)
    brain[4].backward(a)
    for i in range(3,-1,-1):
        brain[i].backward(brain[i + 1].grad_x)
    for i in brain:
        i.update()

    if j % (EPOCH / 20) == 0:
        print()
        print(j + (EPOCH / 20)," / ",EPOCH,"  POINT:",point)
        print(MAP[x - 2:x + 3,y - 2:y + 3])
        print(brain[4].b)
        plot_x.append(j)
        plot_y.append(point)

    MAP[0:5,0:99] = -5
    MAP[95:99,0:99] = -5
    MAP[0:99,0:5] = -5
    MAP[0:99,95:99] = -5
    MAP[6:94,6:94] += 1
    MAP[MAP > 99] = 99

print(ANS - np.sum(MAP),"/",ANS)
plt.scatter(plot_x,plot_y,marker="+")
plt.show()