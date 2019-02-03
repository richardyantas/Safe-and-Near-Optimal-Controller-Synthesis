
import numpy as np
import matplotlib.pyplot as plt
from math import exp,pow


T = 0.1

# Constants
# dm = 0.1 # kg/m3 (Analize if it is variable!!!! for more persons)
# Mc = 100  #kg    -> depends to the volumen
# k(conducticity material espuma de poliuterano) = 16-20 W/(m*ªC) 
# kc = 16
# Irradiance = 20  # W/(m^2*ªC) (Change with the time but it is a reference)
# Ce = 4.186 * 1000 Joule/(kg * ºC) (units?)
# A_stotal = 5.5557 m^2
# A_colector = 1 m^2

# Ie = gauss(5,1)  # calibrate or data !! 
# Tin= gauss(5,1)  # calibrate or data !!
# Te = gauss(5,1)  # calibrate or data !! 


dm  = 0.1
Mc  = 100
Kc  = 16
Ce  = 4.186*1000
A_t = 5.5557
A_c = 1


Ie  = 16*gauss(5,1) 
Tin = 21*gauss(5,1) 
Te  = 24*gauss(5,1)

A1 = (-dm/Mc - Kc*A_t/(Mc*Ce))
g1 = A_c*Ie/(Mc*Ce)+Tin*dm/Mc+Kc*A_c*Te/(Mc*Ce)
u1 = dq/(Mc*Ce)

A2 = (-Kc*A_t)/(Mc*Ce)
g2 = A_c*Ie/(Mc*Ce)+Kc*A_t*Te/(Mc*Ce)
u2 = dq/(Mc*Ce)



# Temperature has 2 modes controlled by valve = ON,OFF (Uncontrollabe)  and Resistance = ON,OFF (Controllable)

# dT/dt = AT + uk + gk

# dq = 5 Watts

# if Vin = ON  -> 1st Mode
#	A1 = (-dm-k2)/Mc
#	g1 = k1*Ie/Mc+Tin*dm/Mc+k2*Te/Mc
#	if R = ON
#		u1 = dq/(Mc*ce)
#	if R = OFF
#		u1 = 0

#if Vin = OFF -> 2nd Mode
#	A2 = (-k2)/Mc
#	g2 = k1*Ie/Mc+k2*Te/Mc
#	if R = ON
#		u2 = dq/(Mc*ce)
#	if R = OFF
#		u2 = 0


# Volume has 3 modes  controlled by setVolumen = {1,2,3} (Stochastic)


# if sV = 1
#	if V > 100
# 		dV/dt = -1(-)                mode 1               
#	if V == 100
# 		dV/dt = 0					 mode 2
# if sV = 2
#	if V > 200
#		dV/dt = -1(-)            mode 1
#   if V = 200
#		dV/dt = 0                mode 2
# 	if V < 200
#		dV/dt = 1(+)             mode 3
#	
# if sV = 3
#	if V<300
# 		dV/dt = 1(+)                 mode 2 
#	if V=300
#		dV/dt = 0					 mode 1


# Question ?
# 1) The change of equation in T and V  can be occur simulaniusly because T depends of Mass(Volumen)
# 2) The energy necessary to change the temperature would be less


def gauss(mean, sig):
	g = np.zeros((100,1))
	for i in range(1,99):
		g[i,0] = 5*(1/(2.5066*sig))*exp(-pow((T*i-mean),2)/(2*pow(sig,2)));
	return g

# dx = -2*x + q(discrete value) 
T = 0.05
dt = 1

tmax = 100
dt = 1
num = tmax/dt
t = np.arange(0, tmax, dt)

x = np.zeros((num,1))
x[1,0] = 1

g = 10*gauss(0.5,3)

for i in range(1,num-1):
	if x[i,0]>2:
		q = 0
	else:
		q = 10
	x[i+1,0] = x[i,0]/(1+2*T) + T*q/(1+2*T) + T*g[i,0]/(1+2*T)




fig, axs = plt.subplots(2, 1)
axs[0].plot(t, x)
axs[0].set_xlim(0, 100)
axs[0].set_xlabel('time')
axs[0].set_ylabel('x')
axs[0].grid(True)

#cxy, f = axs[1].cohere(x, g, 256, 1. / dt)
#axs[1].set_ylabel('coherence')

fig.tight_layout()
plt.show()
