import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from myRK4 import myRK4
from function import *
from GetRK4ReversalTime import getReversalTimes
from plotRK4 import plotRK4

#time/time step
dt = float(input('Enter time step: '))
T = float(input('Enter total time: '))
nSteps = int(T/dt)
#initial condition
print("Enter Initial Condition")
x0_x = float(input('Enter x coordinate: '))
x0_y = float(input('Enter y coordinate: '))
x0_z = float(input('Enter z coordinate: '))
x0 = np.array([[x0_x],[x0_y],[x0_z]])
#RK4 Matrix
x = myRK4(x0,dt,nSteps)
#reversal time vector
reversal_times = getReversalTimes(x, dt)
#plots RK4
plotRK4(x,reversal_times)