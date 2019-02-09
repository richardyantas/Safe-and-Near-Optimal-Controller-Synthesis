
import numpy as np
import matplotlib.pyplot as plt
from math import exp,pow
from utils import sign
from utils import gauss
from utils import signal
from utils import getSec


T   = 1  # importan to gauss 0.1
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