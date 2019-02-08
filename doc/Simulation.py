import numpy as np
import matplotlib.pyplot as plt
from math import exp,pow

# 86400 sec per day
def getSec(hrs):
	return int(hrs*60*60)

def gauss(mean, sig, T, num):
	g = np.zeros((num,1))
	for i in range(1,num-1):
		g[i,0] = 5*(1/(2.5066*sig))*exp(-pow((T*i-mean),2)/(2*pow(sig,2)))
	return g

class signal:
	def __init__(self,num):
		self.g = np.zeros((num,1))
		#print("xd")
	def setOne(self,a,b):
		for i in range(a,b):
			self.g[i,0] = 10
	def setTwo(self,a,b):
		for i in range(a,b):
			self.g[i,0] = 20
	def setThree(self,a,b):
		for i in range(a,b):
			self.g[i,0] = 30

# bang bang controller, and safety controller

T   = 1  # important to gauss 0.1
dm  = 0.1
Mc  = 100
Kc  = 16/4
Ce  = 4.186*1000
A_t = 2.5557
A_c = 2
dq  = 1000 # watts

tmax = 86400
num  = int(tmax/T)
t    = np.arange(0, tmax, T)

Ie  = 1236*5000*gauss(86400/2,86400/4,T,num) 
Tin = 20*gauss(86400/2,86400/4,T,num)
Te  = 28*gauss(86400/2,86400/4,T,num)

x = np.zeros((num,1))
x[1,0] = 20

#print(len(x), len(t))

valveOption = signal(num)
valveOption.setOne(getSec(7),getSec(7.2))
valveOption.setOne(getSec(7.3),getSec(7.5))
resOption   = signal(num)
resOption.setOne(getSec(5),getSec(6))
resOption.setOne(getSec(17),getSec(18))

volOption   = signal(num)
volOption.setThree(getSec(2),getSec(3))
volOption.setOne(getSec(10),getSec(11))
volOption.setThree(getSec(12),getSec(12.5))
volOption.setTwo(getSec(15),getSec(16))
volOption.setOne(getSec(19),getSec(20))




# problems with Units A1 =. 0 d1 =. 0
A1 = (-dm/Mc - Kc*A_t/(Mc*Ce))  # ERROR !! CORRECTION PARENTHESIS!!
d1 = A_c*Ie/(Mc*Ce)+Tin*dm/Mc+Kc*A_t*Te/(Mc*Ce)

A2 = (-Kc*A_t)/(Mc*Ce)
d2 = A_c*Ie/(Mc*Ce)+Kc*A_t*Te/(Mc*Ce)

#A1 = -1
#A2 = -2 

print(A1,A2,dq/(Mc*Ce),np.mean(Ie),np.mean(d1),np.mean(d2))


C1 = Kc*A_t/(Ce*100)
C2 = A_c/(100*Ce)
C3 = dq/(Ce*100)
C4 = 1
# C1 = 2.4421404682274245e-05 
# C2 = 4.777830864787386e-06
# C3 = 0.0023889154323936935
# C4 = 1
print(C1,C2,C3,C4)




y  = np.zeros((num,1))
A1 = np.zeros((num,1))
d1 = np.zeros((num,1))
A2 = np.zeros((num,1))
d2 = np.zeros((num,1))
y[1,0] = 130


for i in range(1,num-1):
	if volOption.g[i,0] == 0:
			y[i+1,0]  = y[i,0]                   # Mode 2	
	if volOption.g[i,0] == 10:
		if y[i,0] > 100:
			y[i+1,0] = y[i,0] - 0.1*T         # Mode 1
		if y[i,0]  <= 100:
			y[i+1,0]  = 100  	
	if volOption.g[i,0] == 20:
		if y[i,0]  > 200:
			y[i+1,0] = y[i,0] - 0.1*T
		if y[i,0] == 200:
			y[i+1,0] = 100 
		if y[i,0] < 200:	
			y[i+1,0] = y[i,0] + 0.1*T         # Mode 3
	if volOption.g[i,0] == 30:		
		if y[i,0] < 300:
			y[i+1,0] = y[i,0] + 0.1*T
		if y[i,0]  >= 300:
			y[i+1,0]  = 300	

	Mc = y[i,0]

	A1[i,0] = (-dm/Mc - Kc*A_t/(Mc*Ce))  # ERROR !! CORRECTION PARENTHESIS!!
	d1[i,0] = A_c*Ie[i,0]/(Mc*Ce)+Tin[i,0]*dm/Mc+Kc*A_t*Te[i,0]/(Mc*Ce)

	A2[i,0] = (-Kc*A_t)/(Mc*Ce)
	d2[i,0] = A_c*Ie[i,0]/(Mc*Ce)+Kc*A_t*Te[i,0]/(Mc*Ce)


for i in range(1,num-1):

	if resOption.g[i,0] != 0:						
		u = dq/(Mc*Ce)
	else:
		u = 0
	if valveOption.g[i,0] != 0:	
		x[i+1,0] = x[i,0]/(1-A1[i,0]*T) + u*T/(1-A1[i,0]*T) + d1[i,0]*T/(1-A1[i,0]*T)
	else:		
		x[i+1,0] = x[i,0]/(1-A2[i,0]*T) + u*T/(1-A2[i,0]*T) + d2[i,0]*T/(1-A2[i,0]*T)


'''
y = np.zeros((num,1))
y[1,0] = 130


for i in range(1,num-1):
	if volOption.g[i,0] == 0:
			y[i+1,0]  = y[i,0]                   # Mode 2	
	if volOption.g[i,0] == 10:
		if y[i,0] > 100:
			y[i+1,0] = y[i,0] - 0.1*T         # Mode 1
		if y[i,0]  <= 100:
			y[i+1,0]  = 100  	
	if volOption.g[i,0] == 20:
		if y[i,0]  > 200:
			y[i+1,0] = y[i,0] - 0.1*T
		if y[i,0] == 200:
			y[i+1,0] = 100 
		if y[i,0] < 200:	
			y[i+1,0] = y[i,0] + 0.1*T         # Mode 3
	if volOption.g[i,0] == 30:		
		if y[i,0] < 300:
			y[i+1,0] = y[i,0] + 0.1*T
		if y[i,0]  >= 300:
			y[i+1,0]  = 300	
'''

fig, axs = plt.subplots(3, 1)
axs[0].plot(t , x, label = 'Temperature')
axs[0].plot(t, valveOption.g, label ='Valve Signal')
axs[0].plot(t,resOption.g , '-r', label = 'Heat Signal')
#axs[0].gca().legend(('Temperature','Valve Signal', 'Heat Signal'))
axs[0].set_xlim(0, getSec(24))
axs[0].legend()
axs[0].set_xlabel('time(Sec)')
axs[0].set_ylabel('Temperature(°C)')
axs[0].grid(True)

#cxy, f = axs[1].cohere(x, g, 256, 1. / dt)
#axs[1].set_ylabel('coherence')

axs[1].plot(t, Ie ,label='Irradiance')
axs[1].plot(t, 100000*Tin ,label='Waterin Temperature x1000')
axs[1].plot(t, 100000*Te ,label='Enviorment Temperature x1000')
axs[1].set_xlim(0, getSec(24))
axs[1].legend(loc=0)
axs[1].set_xlabel('time(sec)')
axs[1].set_ylabel('Perturbations')
axs[1].grid(True)


axs[2].plot(t , y, label = 'Volume')
axs[2].plot(t, volOption.g, label ='Vol Signal')
axs[2].set_xlim(0, getSec(24))
axs[2].legend()
axs[2].set_xlabel('time(Sec)')
axs[2].set_ylabel('Volume(m3)')
axs[2].grid(True)

fig.tight_layout()
plt.show()


