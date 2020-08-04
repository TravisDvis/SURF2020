import matplotlib.pyplot as plt
import numpy as np

from PredictionFunctions import *

def skillSweep(xMatrix,reversal_times):
    
    threshold_vector = np.array([[],[]])

    sweep_parameter = 100
    for i in range(2,sweep_parameter):
        sweep = runPrediction(xMatrix,i/sweep_parameter,reversal_times)
        mcc = sweep[3][0]
        current_threshold = np.array([[i/sweep_parameter],[mcc]])
        threshold_vector = np.append(current_threshold,threshold_vector,axis=1)

    optimal_threshold = threshold_vector[0][np.where(threshold_vector[1][:] == np.amax(threshold_vector[1][:]))]
    print("The optimal threshold(s) is/are: ",optimal_threshold," with an MCC of: ", np.amax(threshold_vector[1][:]))

    ax = plt.axes()
    ax.set(xlabel='Threshold',ylabel='MCC')
    ax.plot(threshold_vector[0][:],threshold_vector[1][:])
    plt.show()
