import numpy as np

from GissengerFunction import *

def RK4Scheme(x0,dt,nSteps):
    #Set initial vector
    x = x0
    xMatrix = x0
    #Initialize time
    t = 0
    #Runke Kutta 4 method
    for kk in range(nSteps):
        #Increment time
        t = t + dt
        #Set k values
        k1 = f(x)
        k2 = f(x + 0.5*dt*k1)
        k3 = f(x + 0.5*dt*k2)
        k4 = f(x + dt*k3)
        #Update x vector
        index_vector = np.array([[0],[0],[0],[dt],[1]])
        x = x + (dt/6)*(k1 + 2*k2 + 2*k3 + k4) + index_vector
        #Append current x vector to the x matrix
        xMatrix = np.append(xMatrix,x,axis = 1)      

    return xMatrix