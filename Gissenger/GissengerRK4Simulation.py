import numpy as np
import matplotlib.pyplot as plt

from FloatExceptionHandle import *
from GissengerFunction import *
from ReversalTimes import *
from PlotRK4 import *
from PredictReversal import *
from mpl_toolkits import mplot3d
from RK4Scheme import *

#time/time step
dt = floatExceptionHandle('Enter time step: ')
T = floatExceptionHandle('Enter total time: ')
nSteps = int(T/dt)
#initial condition
print("Enter Initial Condition")
x0_x = floatExceptionHandle('Enter x coordinate: ')
x0_y = floatExceptionHandle('Enter y coordinate: ')
x0_z = floatExceptionHandle('Enter z coordinate: ')
x0 = np.array([[x0_x],[x0_y],[x0_z]])
#RK4 Matrix
x = myRK4(x0,dt,nSteps)
#reversal time vector
reversal_times = getReversalTimes(x, dt)
#plots RK4
plotRK4(x,reversal_times,dt)
predictReversal(x,0.42)