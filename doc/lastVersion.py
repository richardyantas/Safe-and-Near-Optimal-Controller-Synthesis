
import numpy as np
import matplotlib.pyplot as plt
from math import exp,pow


def gauss(mean, sig, T, num):
	g = np.zeros((num,1))
	for i in range(1,num-1):
		g[i,0] = 5*(1/(2.5066*sig))*exp(-pow((T*i-mean),2)/(2*pow(sig,2)));
	return g

class signal:
	def __init__(self,num):
		self.g = np.zeros((num,1))
		print("xd")
	def setOn(self,a,b):
		for i in range(a,b):
			self.g[i,0] = 10

T   = 1  # importan to gauss 0.1
dm  = 10
Mc  = 100
Kc  = 16*100
Ce  = 4.186*1000
A_t = 5.5557
A_c = 2
dq  = 500000 # watts

tmax = 1000
num  = int(tmax/T)
t    = np.arange(0, tmax, T)

Ie  = 16*gauss(50,1,T,num) 
Tin = 21*gauss(50,1,T,num)
Te  = 24*gauss(50,1,T,num)

x = np.zeros((num,1))
x[1,0] = 20

print(len(x), len(t))

valveOption = signal(num)
valveOption.setOn(10,20)
valveOption.setOn(70,80)
volOption   = signal(num)
volOption.setOn(50,70)
resOption   = signal(num)
resOption.setOn(200,300)


# problems with Units A1 =. 0 d1 =. 0
A1 = (-dm/Mc - Kc*A_t/(Mc*Ce))
d1 = A_c*Ie/(Mc*Ce)+Tin*dm/Mc+Kc*A_t*Te/(Mc*Ce)

A2 = (-Kc*A_t)/(Mc*Ce)
d2 = A_c*Ie/(Mc*Ce)+Kc*A_t*Te/(Mc*Ce)

#A1 = -1
#A2 = -2 
print(A1,A2,dq/(Mc*Ce),np.mean(Ie),np.mean(d1),np.mean(d2))

for i in range(1,num-1):		
	if resOption.g[i,0] != 0:						
		u = dq/(Mc*Ce)
	else:
		u = 0
	if valveOption.g[i,0] != 0:	
		x[i+1,0] = x[i,0]/(1-A1*T) + u*T/(1-A1*T) + d1[i,0]*T/(1-A1*T)
	else:		
		x[i+1,0] = x[i,0]/(1-A2*T) + u*T/(1-A2*T) + d2[i,0]*T/(1-A2*T)


fig, axs = plt.subplots(3, 1)
axs[0].plot(t , x, t, valveOption.g, t, d1, t,resOption.g)
axs[0].set_xlim(0, 1000)
axs[0].set_xlabel('time')
axs[0].set_ylabel('valveOption')
axs[0].grid(True)

#cxy, f = axs[1].cohere(x, g, 256, 1. / dt)
#axs[1].set_ylabel('coherence')

axs[1].plot(t, volOption.g, t, d1, t ,d2)
axs[1].set_xlim(0, 1000)
axs[1].set_xlabel('time')
axs[1].set_ylabel('volOption')
axs[1].grid(True)

axs[2].plot(t, resOption.g)
axs[2].set_xlim(0, 1000)
axs[2].set_xlabel('time')
axs[2].set_ylabel('resOption')
axs[2].grid(True)

fig.tight_layout()
plt.show()


