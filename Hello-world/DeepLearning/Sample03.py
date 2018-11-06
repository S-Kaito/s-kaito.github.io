import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

input_data = np.arange(0,np.pi*2,0.1)
correct_data = np.sin(input_data)
input_data = (input_data - np.pi)/np.pi
n_data = len(correct_data)

n_in = 1
n_mid = 3
n_out = 1

wb_width = 0.01
eta = 0.1
epoch = 3001
interval = 100

class MiddleLayer:
    def __init__(self,n_upper , n):
        self.w = wb_width * np.random.randn(n_upper, n)
        self.b = wb_width * np.random.randn(n)
        
    def forward(self ,x):
        self.x = x
        u = np.dot(x,self.w)  + self.b
        self.y = 1/(1 + np.exp(-u))

    def backward(self,grad_y):
        delta = grad_y * (1-self.y) * self.y
        self.grad_w = np.dot(self.x.T, delta)
        self.grad_b = np.sum(delta, axis=0)
        self.grad_x = np.dot(delta,self.w.T)
        
    def update(self,eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b
    
class OutputLayer:
    def __init__(self, n_upper , n):
        self.w = wb_width * np.random.randn(n_upper, n)
        self.b = wb_width * np.random.randn(n)
        print(self.w.shape)
        
    def forward(self,x):
        self.x = x
        u = np.dot(x,self.w) + self.b
        self.y = u
        
    def backward(self,t):
        delta = self.y - t
        self.grad_w = np.dot(self.x.T , delta)
        self.grad_b = np.sum(delta, axis=0)
        
        self.grad_x = np.dot(delta, self.w.T)
        
    def update(self, eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b
        
middle_layer = MiddleLayer(n_in,n_mid)
output_layer = OutputLayer(n_mid, n_out)

fig = plt.figure()

def plot(i):
    index_random = np.arange(n_data)
    np.random.shuffle(index_random)
    
    total_error = 0
    plot_x = []
    plot_y = []
    
    for idx in index_random:
        x = input_data[idx:idx + 1]
        t = correct_data[idx:idx + 1]

        middle_layer.forward(x.reshape(1,1))
        output_layer.forward(middle_layer.y)

        output_layer.backward(t.reshape(1,1))
        middle_layer.backward(output_layer.grad_x)

        middle_layer.update(eta)
        output_layer.update(eta)

        if i % interval == 0:
            y = output_layer.y.reshape(-1)

            total_error += 1.0/2.0*np.sum(np.square(y-t))

            plot_x.append(x)
            plot_y.append(y)

            plt.cla()
            plt.plot(input_data, correct_data, linestyle="dashed")
            plt.scatter(plot_x,plot_y,marker="+")
        if i % (interval * 10) == 0:
            print(middle_layer.w,middle_layer.b)
            print(output_layer.w,output_layer.b)
            print()

ani = animation.FuncAnimation(fig, plot, interval=1)
plt.show()