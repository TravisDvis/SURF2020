import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def getReversalTimes(xMatrix, dt):
    
    t = 0
    reversal_times = np.array([[],[]])

    for kk in range(np.size(xMatrix,1)-1):

        t = t + dt
        time_index = np.array([[t],[kk]])

        if xMatrix[1][kk] >= 0:
            sign = 0
        else:
            sign = 1

        if kk < np.size(xMatrix,1):
            if sign == 0 and xMatrix[1][kk+1] < 0:
                print("A dipole reversal has occurred at time:",t)
                reversal_times = np.append(reversal_times,time_index,axis=1)
            elif sign == 1 and xMatrix[1][kk+1] >= 0:
                print("A dipole reversal has occurred at time:",t)
                reversal_times = np.append(reversal_times,time_index,axis=1)

    return reversal_times    