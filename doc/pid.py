

import numpy as np
import matplotlib.pyplot as plt
from math import exp,pow

A1 = (-dm-k2)/Mc
g1 = k1*Ie/Mc+Tin*dm/Mc+k2*Te/Mc
u1 = dq/(Mc*ce)

A2 = (-k2)/Mc
g2 = k1*Ie/Mc+k2*Te/Mc
u2 = dq/(Mc*ce)

# mode 1




### Temperatura ##


##################

def resp(kp,ki,kd):
	return 1

print(resp(1,2,3))

kp = 18
ki = 3
kd = 0

dt = 1
t = np.arange(0, 100, dt)
x = np.zeros((100,1))
x[1,0] = 1

mean = 5
sig = 1
T = 0.1

g = np.zeros((100,1))
for i in range(1,99):
	g[i,0] = 5*(1/(2.5066*sig))*exp(-pow((T*i-mean),2)/(2*pow(sig,2)));


s = 0
ref = 5

for i in range(1,99):
	#print(i)
	e = ref - x[i,0]
	s = s + e
	u = e*kp + ki*s

	if i<40:
		x[i+1,0] = x[i,0]/(1+2*T)+T*u/(1+2*T) + g[i,0] 
	else:
		x[i+1,0] = x[i,0]/(1+10*T)+T*u/(1+10*T) + g[i,0]

print(len(g))
print(len(t))

fig, axs = plt.subplots(2, 1)
axs[0].plot(t, x, t, g)
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