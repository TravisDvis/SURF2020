import numpy as np

def getReversalTimes(xMatrix):
    #initializing time and vector
    reversal_times = np.array([[],[]])
    #iterate through RK4 vectors
    for kk in range(np.size(xMatrix,1)-1):
    #logging the sign of the current dipole value
        if xMatrix[1][kk] >= 0:
            sign = 0
        else:
            sign = 1
    #Condition for recognizing a reversal
        if kk < np.size(xMatrix,1):
            if sign == 0 and xMatrix[1][kk+1] < 0:
                time_index = np.array([[xMatrix[3][kk]],[xMatrix[4][kk]]])
                print("A dipole reversal has occurred at time:",xMatrix[3][kk+1])
                reversal_times = np.append(reversal_times,time_index,axis=1)
            elif sign == 1 and xMatrix[1][kk+1] >= 0:
                time_index = np.array([[xMatrix[3][kk]],[xMatrix[4][kk]]])
                print("A dipole reversal has occurred at time:",xMatrix[3][kk+1])
                reversal_times = np.append(reversal_times,time_index,axis=1)
    
    return reversal_times    