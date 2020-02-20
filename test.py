import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from fractions import Fraction

from patterns import *

import random

#cwater = 4177.6  # J/(Kg*K)
#density = 997   # kg/m3
#x1 = cwater*density/1000
#print ( "x1 = %d",x1) #  4165.0672

# We are considering the performance as a constant during the day

    
class state:
    def __init__(self, time, volume, temperature, energyComsuption ):
        self.t = time
        self.V = volume 
        self.T = temperature
        self.E = energyComsuption

class action:
    def __init__(self, piston=0, resistor=0, valve=0, expand = 0):
        # There are 2 cases 
        # 1.- {-1,0,1}  means {D,S,I}
        # 2.- {-1,0,1}  means {Lower Position,K,Upper Position} If it exist.
        #self.pv  = pistonv   #{-1,0,1}
        self.p   = piston
        self.r   = resistor #{0,1}
        self.v   = valve    #{0,1}
        self.f   = expand

class automaton:
    def __init__(self, data):

        self.H   = data['H']  
        self.dt = data['dt'] # Passing to seconds
        self.num = self.H / self.dt + 1        
        self.v   = data['valve']
        self.si  = data['stateInit']
        self.ai  = action()
        self.states  = []
        self.actions = []
        self.actions.append(self.ai)        
        self.states.append(self.si)
        self.d = data['D']        
        self.target = data['Target']
        self.rate_volume_change = 0.0002
# 0.193  
 

    def controller(self,s):
        patterns = query(s)    
        size = len(patterns)        
        n = random.randint(0,size-1)
        #print( len(patterns[n]), " ", patterns[n].item(2) )
        return patterns[n]

    def simulation(self):
        fe = 2.5
        s = self.si        
        dt = self.dt
        mode = action()
        tau = 5*60
        num_tau = tau/dt
        modes = []
        modes.append( action(1,0,0,0) )
        modes.append( action(1,1,0,0) )
        modes.append( action(2,0,0,0) )
        modes.append( action(2,1,0,0) )
        modes.append( action(6,0,0,1) )
        modes.append( action(6,1,0,1) )
        modes.append( action(2,0,0,1) )
        modes.append( action(2,1,0,1) )        
        k = 0
        pattern = np.matrix([[0, 1, 2]])
        pattern = self.controller(s)
        for i in range(0,self.num-1):            
            if i%(num_tau) == 0:  # Tau = 5 min to control supervise
                if (k<3 and pattern.item(k) == -1) or k>2:
                    pattern = self.controller(s)
                    #print(len(pattern[0]))
                    k = 0    
                mode = modes[ pattern.item(k)]     
                k = k + 1              
            E = s.E + dt*mode.r*2  # dt = 0.1
            V = s.V + dt*0.01*( 0.1*mode.p - s.V ) # 0.5 = rate    
            T = s.T + dt*(1/(0.1*mode.p))*( 
                        - fe*2.8811059759131854e-06*(s.T-self.d['Te'][i]) 
                        - mode.v*9.34673995175876e-05*(s.T-self.d['Ti'][i])
                        - mode.f*0.001005026*(0.1*mode.p-V)*(s.T-self.d['Ti'][i])
                        + 8.403225763080125e-07*self.d['I'][i]
                        + mode.r*0.00048018432931886426 )
            t = s.t + dt
            s = state(t,V,T,E)
            #s = self.post(s,a,i)
            #Plot actions
            self.actions.append(mode)  
            self.states.append( s )
    
    def getT(self):
        T = []
        for i in A.states:
            T.append(i.T)
        return T

    def getV(self):
        V = [] 
        for i in A.states:
            V.append(i.V)            
        return V

    def getE(self):
        E = [] 
        for i in A.states:
            E.append(i.E)            
        return E

    def getTime(self):
        time = [] 
        for i in A.states:
            time.append(i.t)            
        return time

    def getr(self):
        r = []
        for i in A.actions:
            r.append(i.r)
        return r
    
    def getp(self):
        p = []
        for i in A.actions:
            p.append(i.p+4)
        return p

    def getv(self):
        v = []
        for i in A.actions:
            v.append(i.v+2)
        return v


            
dataRead = pd.read_csv("Solargis_min15_Almeria_Spain.csv")
valveRead= pd.read_csv("valve.csv")  # t1,t2,dur


dt_ = 15*60           # Real time of the data 
Horizont = 1*24*60*60      # Real time Interval from  [0-Horizont]
num_ = Horizont/dt_    # Num of intervals         [0 - num*tau]  , but there are num+1 points  t[0] - t[num]
t_  = np.linspace(0,Horizont,num_+1)
T_e = dataRead['Temperature'].values.tolist()[0:num_+1]
I_  = dataRead['GTI'].values.tolist()[0:num_+1]
v_  = valveRead['Flow'].values.tolist()[0:num_+1] 

print(len(t_))
print(len(I_))
print(len(v_))

dt = 60
num = Horizont/dt
t   = np.linspace(0,Horizont,num+1)
Te  = np.interp(t,t_,T_e)
I   = np.interp(t,t_,I_)
v   = np.interp(t,t_ ,v_)
Ti  = np.ones(num+1)*15


#print(len(Ti))


data = {
    'dt' : dt,  # Passing to seconds from hours
    'H'   : Horizont,# Passing to seconds from hours  2976*15*60
    'num' : num,
    'D'   : {
                'Te'  : Te, #dataRead['Temperature'].values.tolist()[0:num],
                'Ti'  : Ti,
                'I'   : I,
            },
    
    'valve': v,
    'Target': {
                'Td' : 40,   # 21 temperatura de comfort humano
                'Vd' : 100,
              },
    
    'stateInit': state(0,2*100*0.001,51,0)
}


A = automaton(data)
A.simulation()
#t = [] 
#for i in A.getTime():
#    t.append( float(Fraction(i,3600)) )

# print("time: %d, T: %d, Te: %d",len(t),len(T),len(Te))


print( len(t) , len(data['D']['I']) , len(A.getT()) )


#plt.figure( figsize=(11, 9))



fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('time(s)')
ax1.set_ylabel('Enviornment Temperature', color = color)
ax1.plot(t,data['D']['Te'], color=color)
ax1.tick_params(axis='y', labelcolor = color)
plt.grid(True)
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Irradiance', color=color)
ax2.plot(t,data['D']['I'],color = color)
ax2.tick_params(axis='y',labelcolor=color)




#plt.plot(t, data['D']['Te'],label='Te')
#plt.ylabel('Te(Celsius)')
#plt.xlabel('time(hrs)')
#plt.legend()


plt.figure( figsize=(11, 11))

grid = plt.GridSpec(4, 4, wspace=0.8, hspace=0.7)


plt.subplot( grid[0,:2] )
plt.plot(t, A.getT() ,label='T')
plt.ylabel('T(Celsius)')
plt.xlabel('time(hrs)')
plt.legend()
plt.grid(True)

plt.subplot( grid[1,:2] )
plt.plot(t,A.getV(),label='T')
plt.ylabel('V(L)')
plt.xlabel('time(hrs)')
plt.legend()
plt.grid(True)

plt.subplot( grid[1:3,2:4] )
plt.plot(A.getT(),A.getV(),'black')
plt.ylabel('V(L)')
plt.xlabel('T(Celsius)')
plt.legend()
plt.grid(True)

plt.subplot( grid[2,:2] )
plt.plot(t,A.getE(),'r')
plt.ylabel('E(kJ)')
plt.xlabel('time(Hrs)')
plt.legend()
plt.grid(True)


# but have shapes (2881,) and (576,)

plt.subplot( grid[3,:2] )
plt.plot(t,A.getr(),'r')
plt.plot(t,A.getv(),'g')
plt.plot(t,A.getp(),'b')

plt.axis([0,Horizont,0,8])
plt.ylabel('{r,v,p}')
plt.xlabel('time(Hrs)')
plt.legend()
plt.grid(True)

plt.show()


'''
    Tree Strategy

    1. Data collected interpolate from 100 to 1000 points which a tau beetwen points to 1minute
        1.1 we have 10 points with tau = 15min if we changue tau tovalve 1 min then we have 100*15
        1.2 
    2. 
    p,r    
    0:  1,0
    1:  1,1
    2:  2,0
    3:  2,1
    4:  3,0
    5:  3,1
    6:  2,0
    7:  2,1
    if s.T < self.target['Td']:
            r = 1
            if s.V <= 0.1:
                p = 0
            else:
                p = -1
        if s.T > self.target['Td']:
            r = 0
            if s.V >= 0.3:
                p = 0
            else:
                p = 1
        v = 0
    '''
    

