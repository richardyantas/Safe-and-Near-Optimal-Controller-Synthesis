
import numpy as np
import matplotlib.pyplot as plt
from math import exp,pow


def sign(x):
    if x<0:
        return -1
    if x == 0:
        return 0
    if x>0:
        return 1

def getSec(hrs):
	return int(hrs*60*60)

def gauss(mean, sig, T, num):
	g = np.zeros((num,1))
	for i in range(1,num-1):
		g[i,0] = 5*(1/(2.5066*sig))*exp(-pow((T*i-mean),2)/(2*pow(sig,2)))
	return g


class resistance:
	def __init__(self,num):
		self.g = np.zeros((num,1))
	def setOneValues(self,a,b):
		for i in range(a,b):
			self.g[i,0] = 1

class valve:
	def __init__(self,num):
		self.g = np.zeros((num,1))
	def setOneValues(self,a,b):
		for i in range(a,b):
			self.g[i,0] = 1


class piston:
	def __init__(self,num):
		self.g = np.ones((num,1))
	def setTwoValues(self,a,b):
		for i in range(a,b):
			self.g[i,0] = 2
	def setThreeValues(self,a,b):
		for i in range(a,b):
			self.g[i,0] = 3
