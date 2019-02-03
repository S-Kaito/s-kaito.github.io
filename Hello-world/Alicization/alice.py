import numpy as np
import random
import sys
import tensorflow as tf
import tkinter

from abc import ABCMeta , abstractmethod

WEIGHT = 0.1
ETA = 0.01
class env:
	def __init__(this):
		this.map = np.zeros((100,100),dtype=int)
		this.x = 50
		this.y = 50
		this.turn = 0

		this.width = 100
		this.height = 100
		this.reset()

	def reset(this):
		this.map = np.zeros((100,100),dtype=int)
		for i in range(7):
			xx = random.randint(15,85)
			yy = random.randint(15,85)
			for j in range(10):
				this.map[xx - j:xx + j,yy - j:yy + j] -= 2
		for i in range(7):
			xx = random.randint(15,85)
			yy = random.randint(15,85)
			for j in range(10):
				this.map[xx - j:xx + j,yy - j:yy + j] += 2
		ANS = np.sum(this.map[this.map > 0])

		this.x = 50
		this.y = 50
		this.turn = 0

		this.width = 100
		this.height = 100
		observation = [this.x,this.y]
		observation += [item for sublist in this.map[this.x - 2:this.x + 3] for item in sublist[this.y - 2:this.y + 3]]
		return observation

	def step(this,action):

		observation = None
		reward = 0
		done = False
		info = {}

		this.map[0:10,:] = -20
		this.map[-10:,:] = -20
		this.map[:,0:10] = -20
		this.map[:,-10:] = -20
		this.map[this.map > 20] = 20
		this.map[this.map < -20] = -20
		
		if action == 0:
			this.y -= 1
		elif action == 1:
			this.y += 1
		elif action == 2:
			this.x += 1
		elif action == 3:
			this.x -= 1

		reward += this.map[this.x][this.y]
		this.map[this.x][this.y] = 0
		observation = [this.x,this.y]
		observation += [item for sublist in this.map[this.x - 2:this.x + 3] for item in sublist[this.y - 2:this.y + 3]]
		
		if (this.x == 5 or this.x == this.width - 5) or (this.y == 5 or this.y == this.height - 5):
			done = True
			
		return observation,reward,done,info

	def render(this):
		root = tkinter.Tk()
		root.title("this.map result")
		root.geometry("500x500")

		canvas = tkinter.Canvas(root, width = 500, height = 500)#Canvasの作成
		
		for i in range(this.width):
			for j in range(this.height):
				if this.map[i][j] < -10:
					canvas.create_rectangle(i * 5, j * 5, i * 5 + 5,j * 5 + 5, fill = '#FF0000')#塗りつぶし
				elif this.map[i][j] < 0:
					canvas.create_rectangle(i * 5, j * 5, i * 5 + 5,j * 5 + 5, fill = '#FF8888')#塗りつぶし
				elif this.map[i][j] == 0:
					canvas.create_rectangle(i * 5, j * 5, i * 5 + 5,j * 5 + 5, fill = '#FFFFFF')#塗りつぶし
				elif this.map[i][j] < 10:
					canvas.create_rectangle(i * 5, j * 5, i * 5 + 5,j * 5 + 5, fill = '#88FF88')#塗りつぶし
				else:
					canvas.create_rectangle(i * 5, j * 5, i * 5 + 5,j * 5 + 5, fill = '#00FF00')

		canvas.place(x=0, y=0)#Canvasの配置
		root.mainloop()