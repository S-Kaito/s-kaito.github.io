
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter

INPUT_DATA = np.linspace(-1.0,1.0,100)
OUTPUT_DATA = np.sin(INPUT_DATA * np.pi)
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

def event():
    global EPOCH

    EPOCH -= 1
    for i in INPUT_DATA:
        layer.forward(np.array([i]).reshape(1,1))
        output.forward(layer.y)

        output.backward(OUTPUT_DATA[np.where(INPUT_DATA == i)].reshape(1,1))
        layer.backward(output.grad_x)

        layer.update()
        output.update()

    if EPOCH % 20 == 0:    
        print(layer.w,layer.b)
        print(output.w,output.b)

    layer_b = layer.b.tolist()
    layer_w = layer.w.tolist()
    output_w = output.w.tolist()
    output_b = output.b.tolist()

    canvas.create_line(350,100,150,350,fill=getColor(layer_w[0][0]),width=3.0)
    canvas.create_line(350,100,350,350,fill=getColor(layer_w[0][1]),width=3.0)
    canvas.create_line(350,100,550,350,fill=getColor(layer_w[0][2]),width=3.0)

    canvas.create_line(150,350,350,550,fill=getColor(output_w[0][0]),width=3.0)
    canvas.create_line(350,350,350,550,fill=getColor(output_w[1][0]),width=3.0)
    canvas.create_line(550,350,350,550,fill=getColor(output_w[2][0]),width=3.0)

    canvas.create_oval(100,300,200,400,fill=getColor(layer_b[0]))
    canvas.create_oval(300,300,400,400,fill=getColor(layer_b[1]))
    canvas.create_oval(500,300,600,400,fill=getColor(layer_b[2]))

    canvas.create_oval(300,500,400,600,fill=getColor(output_b[0]))

    if EPOCH > 0:
        root.after(10,event)

def getColor(n):
    if n < -1:
        return "#FF0000"
    elif n < -0.25:
        return "#FF8888"
    elif n < 0.25:
        return "#FFFFFF"
    elif n < 1:
        return "#88FF88"
    else:
        return "#00FF00"

root = tkinter.Tk()
root.geometry("700x700")
canvas = tkinter.Canvas(root,width=700,height=700)
canvas.place(x=0,y=0)
root.after(10,event)
root.mainloop()