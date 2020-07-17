import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

def plotRK4(xMatrix,reversal_times):
    #Initialize 3D plot
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    #Iterate through RK4 matrix
    for kk in range(np.size(xMatrix,1)-1):
        #Plot RK4 values
        ax.scatter3D(xMatrix[0][kk],xMatrix[1][kk],xMatrix[2][kk], 'gray')
        for tt in range(np.size(reversal_times,1)):
            #Condition for recognizing reversal time
            if kk == reversal_times[1][tt]: 
                #Plot vertical line when reversal occurs
                x_t = np.linspace(xMatrix[0][kk],xMatrix[0][kk],10)
                y_t = np.linspace(xMatrix[1][kk],xMatrix[1][kk],10)
                z_t = np.linspace(-5,5,10)
                ax.plot3D(x_t,y_t,z_t, 'red')
    #Show plot
    plt.show()