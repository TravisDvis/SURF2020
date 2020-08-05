import numpy as np

from GissengerFunction import *

def RK4Scheme(x0,dt,nSteps):
    #Set initial vector
    x = x0
    xMatrix = x0
    #Runke Kutta 4 method
    for kk in range(nSteps):
        #Set k values
        k1 = f(x)
        k2 = f(x + 0.5*dt*k1)
        k3 = f(x + 0.5*dt*k2)
        k4 = f(x + dt*k3)
        #Update x vector
        x = x + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
        #Append current x vector to the x matrix
        xMatrix = np.append(xMatrix,x,axis = 1)

    return xMatrix