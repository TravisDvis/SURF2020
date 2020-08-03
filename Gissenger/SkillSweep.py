import matplotlib.pyplot as plt
import numpy as np

from PredictionFunctions import *

def skillSweep(xMatrix,reversal_times):
    
    threshold_vector = np.array([])
    mcc_vector = np.array([])

    sweep_parameter = 100
    for i in range(2,sweep_parameter):
        sweep = runPrediction(xMatrix,i/sweep_parameter,reversal_times)
        mcc = sweep[3][0]
        threshold_vector = np.append(threshold_vector,i/sweep_parameter)
        mcc_vector = np.append(mcc_vector,mcc)

    ax = plt.axes()
    ax.set(xlabel='Threshold',ylabel='MCC')
    ax.plot(threshold_vector,mcc_vector)
    plt.show()
