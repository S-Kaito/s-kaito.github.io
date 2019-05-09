import numpy as np
import matplotlib.pyplot as plt
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
		
		mapData = []

		for i in range(this.width):
			row = []
			for j in range(this.height):
				tip = [255,255,255]
				if this.map[i][j] < 0:
					tip = [255 * (this.map[i][j] / -20),0,0]
				elif this.map[i][j] > 0:
					tip = [0,255 * (this.map[i][j] / 20),0]
				if this.x == i and this.y == j:
					tip = [0,0,255]
				row.append(tip)
			mapData.append(row)
		return mapData
