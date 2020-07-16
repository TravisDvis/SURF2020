import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from myRK4 import myRK4
from function import *
from GetRK4ReversalTime import getReversalTimes

dt = 0.1
T = 1000
nSteps = int(T/dt)

#initial condition
x0 = np.array([[1],[2],[3]])

x = myRK4(x0,dt,nSteps)

reversal_times = getReversalTimes(x, dt)

fig = plt.figure()
ax = plt.axes(projection = '3d')

for kk in range(nSteps):
    ax.scatter3D(x[0][kk],x[1][kk],x[2][kk], 'gray')
    for tt in range(np.size(reversal_times,1)):
        if kk == reversal_times[1][tt]: 
            x_t = np.linspace(x[0][kk],x[0][kk],1000)
            y_t = np.linspace(x[1][kk],x[1][kk],1000)
            z_t = np.linspace(-5,5,1000)
            ax.plot3D(x_t,y_t,z_t, 'gray')

plt.show()