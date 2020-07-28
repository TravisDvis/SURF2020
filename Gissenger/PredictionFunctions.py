import numpy as np

def positiveToNegative(kk,xMatrix,threshold):

    global increase

    if xMatrix[1][kk] <= threshold and xMatrix[1][kk] >= 0:
        reversal_prediction = True
    else:
        reversal_prediction = False
        
    for i in range(kk,np.size(xMatrix,1)-1):
        if xMatrix[1][i] <= xMatrix[1][i+1]:
            increase = xMatrix[1][i]
            temp_index = i
            break
        increase = xMatrix[1][i]

    if increase <= 0:
        reversal = True
        kk = temp_index
    else:
        reversal = False
      
    if reversal_prediction == True and reversal == True:
        print("True Positive")
        return 0
    elif reversal_prediction == False and reversal == False:
        print("True Negative")
        return 1
    elif reversal_prediction == True and reversal == False:
        print("False Positive")
        return 2
    elif reversal_prediction == False and reversal == True:
        print("False Negative")
        return 3

        
def negativeToPositive(kk,xMatrix,threshold):
    
    global decrease
    neg_threshold = np.negative(threshold)

    if xMatrix[1][kk] >= neg_threshold and xMatrix[1][kk] < 0:
        reversal_prediction = True
    else:
        reversal_prediction = False
        
    for i in range(kk,np.size(xMatrix,1)-1):
        if xMatrix[1][i] >= xMatrix[1][i+1]:
            decrease = xMatrix[1][i]
            temp_index = i
            break
        if i == np.size(xMatrix,1)-2:
            decrease = xMatrix[1][i]
            break
    
    if decrease >= 0:
        reversal = True
        kk = temp_index
    else:
        reversal = False
      
    if reversal_prediction == True and reversal == True:
        print("True Positive")
        return 0
    elif reversal_prediction == False and reversal == False:
        print("True Negative")
        return 1
    elif reversal_prediction == True and reversal == False:
        print("False Positive")
        return 2
    elif reversal_prediction == False and reversal == True:
        print("False Negative")
        return 3