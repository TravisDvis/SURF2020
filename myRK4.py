import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from function import *

def myRK4(x0,dt,nSteps):
    
    t = 0
    timeVector = np.array([t])

    x = x0
    xMatrix = x0

    for kk in range(nSteps):

        t = t + dt

        k1 = f(x)
        k2 = f(x + 0.5*dt*k1)
        k3 = f(x + 0.5*dt*k2)
        k4 = f(x + dt*k3)

        x = x + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

        xMatrix = np.append(xMatrix,x,axis = 1)
        timeVector = np.append(timeVector,t)

    return xMatrix