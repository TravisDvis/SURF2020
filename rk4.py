import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from myRK4 import myRK4
from function import *

dt = 0.1
T = 1000
nSteps = int(T/dt)

#initial condition
x0 = np.array([[1],[2],[3]])

x = myRK4(x0,dt,nSteps)

fig = plt.figure()
ax = plt.axes(projection = '3d')

for kk in range(nSteps):
    ax.scatter3D(x[0][kk],x[1][kk],x[2][kk], 'gray')

plt.show()