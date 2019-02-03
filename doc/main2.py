import numpy as np
import matplotlib.pyplot as plt
from math import exp,pow

def gauss(mean, sig):
	g = np.zeros((100,1))
	for i in range(1,99):
		g[i,0] = 5*(1/(2.5066*sig))*exp(-pow((T*i-mean),2)/(2*pow(sig,2)));
	return g


kp = 18
ki = 3
kd = 0

dt = 1
t = np.arange(0, 100, dt)
x = np.zeros((100,1))
x[1,0] = 1

T = 0.1

dm = 0.1 # kg/m3
Mc = 100  #kg
k1 = 50
k2 = 20  # W/mªC
ce = 3

Ie = gauss(5,1) 
Tin= gauss(5,1)
Te = gauss(5,1)


A1 = (-dm-k2)/Mc
g1 = k1*Ie/Mc+Tin*dm/Mc+k2*Te/Mc
B1 = 1/(Mc*ce)
#u1 = dq

A2 = (-k2)/Mc
g2 = k1*Ie/Mc+k2*Te/Mc
B2 = 1/(Mc*ce)
#u2 = dq

s = 0
ref = 5

for i in range(1,99):
	#print(i)
	e = ref - x[i,0]
	s = s + e
	if i<40:
		u1 = e*kp + ki*s
		x[i+1,0] = x[i,0]/(1-A1*T)+T*B1*u1/(1-A1*T) + T*g1[i,0]/(1-A1*T) 
	else:
		u2 = e*kp + ki*s
		x[i+1,0] = x[i,0]/(1-A2*T)+T*B2*u2/(1-A2*T) + T*g2[i,0]/(1-A2*T)

#print(len(g))
#print(len(t))

fig, axs = plt.subplots(2, 1)
axs[0].plot(t, x, t, g2)
axs[0].set_xlim(0, 100)
axs[0].set_xlabel('time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)

#cxy, f = axs[1].cohere(x, g, 256, 1. / dt)
#axs[1].set_ylabel('coherence')

fig.tight_layout()
plt.show()



#plt.plot(t,x,t,g)
#plt.grid(True, lw = 1, ls = '--', c = '.75')
#plt.show()