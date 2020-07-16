import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from myRK4 import myRK4
from function import *
from GetRK4ReversalTime import getReversalTimes
from plotRK4 import plotRK4

#time/time step
dt = 0.1
T = 1000
nSteps = int(T/dt)
#initial condition
x0 = np.array([[1],[2],[3]])
#RK4 Matrix
x = myRK4(x0,dt,nSteps)
#reversal time vector
reversal_times = getReversalTimes(x, dt)
#plots RK4
plotRK4(x,reversal_times)