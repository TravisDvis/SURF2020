import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits import mplot3d
from PredictionFunctions import *

def skillSweep(xMatrix,reversal_times,dt):
    #Initialize threshold vector
    threshold_vector = np.array([[],[],[]])
    #Number of steps minus 2
    sweep_parameter = 50
    #Sweep of thresholds
    for i in range(1,sweep_parameter):
        for j in range(1,sweep_parameter):
            sweep = runPrediction(xMatrix,i/sweep_parameter,j/sweep_parameter,reversal_times,dt)
            mcc = sweep[3][0]
            if mcc == 0:
                continue
            current_threshold = np.array([[i/sweep_parameter],[j/sweep_parameter],[mcc]])
            threshold_vector = np.append(current_threshold,threshold_vector,axis=1)

    #Indicate optimal threshold
    optimal_threshold_pos = threshold_vector[0][np.where(threshold_vector[2][:] == np.amax(threshold_vector[2][:]))]
    optimal_threshold_neg = threshold_vector[1][np.where(threshold_vector[2][:] == np.amax(threshold_vector[2][:]))]
    print("The optimal positive threshold(s) is/are: ",optimal_threshold_pos,", and the optimal negative threshold(s) is/are: ",optimal_threshold_neg," with an MCC of: ",np.amax(threshold_vector[2][:]))
    #Plot Threshold values vs MCC
    ax = plt.axes(projection = '3d')
    ax.set(xlabel='Positive Threshold',ylabel='Negative Threshold',zlabel='MCC')
    ax.plot3D(threshold_vector[0][:],threshold_vector[1][:],threshold_vector[2][:], 'go', label='MCC vs Thresholds')
    plt.show()
