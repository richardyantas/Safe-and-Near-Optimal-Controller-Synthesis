
import numpy as np
import matplotlib.pyplot as plt
from utils import *

T   = 1  # importan to gauss 0.1
dm  = 0.1
Mc  = 100
Kc  = 16/4
Ce  = 4.186*1000
A_t = 2.5557
A_c = 2
dq  = 1000 # watts
# 
tmax= 86400
num = int(tmax/T)
t   = np.arange(0, tmax, T)
Ie  = 1236*5000*gauss(86400/2,86400/4,T,num) 
Tin = 20*gauss(86400/2,86400/4,T,num)
Te  = 28*gauss(86400/2,86400/4,T,num)

x = np.zeros((num,1))	
y = np.zeros((num,1))
A = np.zeros((num,1))
d = np.zeros((num,1))

x[1,0] = 20
y[1,0] = 130

va = valve(num)
va.setOneValues(getSec(7),getSec(7.2))
va.setOneValues(getSec(7.3),getSec(7.5))

re = resistance(num)
re.setOneValues(getSec(5),getSec(6))
re.setOneValues(getSec(17),getSec(18))

vo = piston(num)
vo.setThreeValues(getSec(2),getSec(6))
vo.setTwoValues(  getSec(15),getSec(16))

#   

# y[1,0] = 130

vp = 0.1 # Piston velocity 

for i in range(1,num-1):
    if abs(y[i,0]-100*vo.g[i,0]) <= 0:
        y[i+1,0] = y[i,0]  
    else:
        y[i+1,0] = y[i,0] - vp*T*sign( y[i,0]-100*vo.g[i,0] )            
    Mc = y[i,0]
    A[i,0]  =  ( va.g[i,0]*(-dm/Mc) - Kc*A_t/(Mc*Ce) )
    d[i,0]  =  A_c*Ie[i,0]/(Mc*Ce) + va.g[i,0]*Tin[i,0]*dm/Mc + Kc*A_t*Te[i,0]/(Mc*Ce)
    x[i+1,0]=  x[i,0]/(1-A[i,0]*T) + re.g[i,0]*dq/(Mc*Ce)*T/(1-A[i,0]*T) + d[i,0]*T/(1-A[i,0]*T)

fig, axs = plt.subplots(3, 1)
axs[0].plot(t , x, label = 'Temperature')
axs[0].plot(t , y/10, label = 'Volume')
axs[0].plot(t, 10*va.g, label ='Valve Signal')
axs[0].plot(t, 10*re.g , '-r', label = 'Heat Signal')
axs[0].set_xlim(0, getSec(24))
axs[0].legend()
axs[0].set_xlabel('time(Sec)')
axs[0].set_ylabel('Temperature(°C)')
axs[0].grid(True)


axs[1].plot(t, Ie ,label='Irradiance')
axs[1].plot(t, 100000*Tin ,label='Waterin Temperature x1000')
axs[1].plot(t, 100000*Te ,label='Enviorment Temperature x1000')
axs[1].set_xlim(0, getSec(24))
axs[1].legend(loc=0)
axs[1].set_xlabel('time(sec)')
axs[1].set_ylabel('Perturbations')
axs[1].grid(True)


axs[2].plot(t , y, label = 'Volume')
axs[2].plot(t, 10*vo.g, label ='Vol Signal')
axs[2].set_xlim( 0, getSec(24) )
axs[2].legend()
axs[2].set_xlabel('time(Sec)')
axs[2].set_ylabel('Volume(m3)')
axs[2].grid(True)

fig.tight_layout()
plt.show()