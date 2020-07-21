import numpy as np

def predictReversal(xMatrix,positive_threshold,negative_threshold):
    #positive to negative
    for kk in range(np.size(xMatrix,1)):
        
        if xMatrix[1][kk] <= positive_threshold and xMatrix[1][kk] >= 0:
            reversal_prediction = True
        else:
            reversal_prediction = False
            continue
        
        tt = kk
        for tt in range(np.size(xMatrix,1)):
            if xMatrix[1][tt-1] > xMatrix[1][tt]:
                continue
            else:
                increase = xMatrix[1][tt]
                temp_index = tt
                break
        
        if increase >= 0:
            prediction = False
        else:
            prediction = True
            kk = temp_index

        if reversal_prediction == True and prediction == True:
            print("True Positive")
        elif reversal_prediction == False and prediction == False:
            print("True Negative")
        elif reversal_prediction == True and prediction == False:
            print("False Positive")
        elif reversal_prediction == False and prediction == True:
            print("False Negative")
        