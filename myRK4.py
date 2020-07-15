import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from function import *

def myRK4(x0,dt,nSteps):
    
    x = x0
    xMatrix = x0

    t = 0
    reversal_times = np.array([])

    for kk in range(nSteps):
        
        t = t + dt

        k1 = f(x)
        k2 = f(x + 0.5*dt*k1)
        k3 = f(x + 0.5*dt*k2)
        k4 = f(x + dt*k3)
        
        if x[1] >= 0:
            sign = 0
        else:
            sign = 1

        x = x + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

        if sign == 0 and x[1] < 0:
            print("A dipole reversal has occurred")
            print(t)
            reversal_times = np.append(reversal_times,t)
            print(reversal_times)            

        elif sign == 1 and x[1] >= 0:
            print("A dipole reversal has occurred")
            print(t)
            reversal_times = np.append(reversal_times,t)
            print(reversal_times)

        xMatrix = np.append(xMatrix,x,axis = 1)

    return xMatrix