
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d
from Rescale import *

def plotRK4(xMatrix,reversal_times):
    #Rescale?
    rescaled_xMatrix = rescale(xMatrix)
    #Initialize 3D plot
    ax = plt.axes(projection = '3d')
    ax.set(xlabel='Q',ylabel='D',zlabel='V')
    Q_t = rescaled_xMatrix[0][:]
    D_t = rescaled_xMatrix[1][:]
    V_t = rescaled_xMatrix[2][:]
    t = rescaled_xMatrix[3][:]
    #Plotting RK4
    ax.plot3D(Q_t,D_t,V_t, 'go', label='G12 Model')
    #Time Reversal Detection
    for kk in range(np.size(rescaled_xMatrix,1)):
        for tt in range(np.size(reversal_times,1)):
    #Condition for recognizing reversal time
            if kk == reversal_times[1][tt]: 
    #Plot vertical line when reversal occurs
                x_t = np.linspace(rescaled_xMatrix[0][kk],rescaled_xMatrix[0][kk],10)
                y_t = np.linspace(rescaled_xMatrix[1][kk],rescaled_xMatrix[1][kk],10)
                z_t = np.linspace(-5,5,10)
                ax.plot3D(x_t,y_t,z_t,label='Reversal Occurence #'+str(tt))
    ax.legend()
    #Setting up plotting Q,D,V as individual subplots
    figsub, (ax1,ax2,ax3) = plt.subplots(3)
    figsub.suptitle('Quadrupole, Velocity, and Dipole')
    #labeling axes
    ax1.set(ylabel='Q')
    ax2.set(ylabel='D')
    ax3.set(xlabel='time', ylabel='V')
    #Plot Q
    ax1.plot(t,Q_t)
    #Plot D
    ax2.plot(t,D_t)
    #Plot vertical lines when reversals occur
    for tt in range(np.size(reversal_times,1)):
        ax2.vlines(reversal_times[0][tt], -2.5, 2.5, colors='r')
    #Plot V
    ax3.plot(t,V_t)
    #Show plot
    plt.show()


    