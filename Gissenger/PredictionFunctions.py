import math
import numpy as np

def runPrediction(xMatrix,threshold,reversal_times):

    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    reversal_curve = reversalCurve(xMatrix,threshold,reversal_times)

    for kk in range(np.size(xMatrix,1)):
        
        if xMatrix[1][kk] <= threshold and xMatrix[1][kk] >= -1*threshold:
            reversal_prediction = True
        else:
            reversal_prediction = False
        
        if reversal_prediction == True and reversal_curve[kk] == 1:
            true_positive = true_positive + 1
        elif reversal_prediction == False and reversal_curve[kk] == 0:
            true_negative = true_negative + 1
        elif reversal_prediction == True and reversal_curve[kk] == 0:
            false_positive = false_positive + 1
        elif reversal_prediction == False and reversal_curve[kk] == 1:
            false_negative = false_negative + 1

    acc = (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative)
    
    f1 = (2*true_positive)/(2*true_positive + false_positive + false_negative)

    csi = (true_positive)/(true_positive + false_positive + false_negative)

    mcc_num = ((true_positive*true_negative)-(false_positive*false_negative))
    mcc_den = math.sqrt((true_positive + false_positive)*(true_positive + false_negative)*(true_negative + false_positive)*(true_negative + false_negative))
    mcc = mcc_num/mcc_den

    skill_scores = np.array([[acc],[f1],[csi],[mcc]])

    return skill_scores            


def reversalCurve(xMatrix,threshold,reversal_times):
    
    reversal_curve = np.zeros(np.size(xMatrix,1))

    for i in range(np.size(xMatrix,1)):
        for ii in range(np.size(reversal_times,1)):
            if i == reversal_times[1][ii]:
                reversal_curve[i-2] = 1
                reversal_curve[i-1] = 1
                reversal_curve[i] = 1
                reversal_curve[i+1] = 1
                reversal_curve[i+2] = 1
                break         
            
    return reversal_curve
    
def crossThreshold(xMatrix,threshold):
        
    crossed_threshold = np.array([])
   
    for kk in range(np.size(xMatrix,1)-1):
        
        if xMatrix[1][kk] > threshold or xMatrix[1][kk] < -1*threshold:
            sign = 0
        else:
            sign = 1
        
        if sign == 0 and (xMatrix[1][kk+1] <= threshold and xMatrix[1][kk+1] >= -1*threshold):
            crossed_threshold = np.append(crossed_threshold,kk)
        elif sign == 1 and (xMatrix[1][kk+1] > threshold or xMatrix[1][kk+1] < -1*threshold):
            crossed_threshold = np.append(crossed_threshold,kk)

    return crossed_threshold

def crossAndReversed(xMatrix,threshold,reversal_times):
    
    crossed_threshold = crossThreshold(xMatrix,threshold)
    crossed_and_reversed = np.array([])

    for i in range(np.size(crossed_threshold)-1):
        for ii in range(np.size(reversal_times,1)):
            if reversal_times[1][ii] > crossed_threshold[i] and reversal_times[1][ii] < crossed_threshold[i+1]:
                crossed_and_reversed = np.append(crossed_and_reversed,crossed_threshold[i])
                if i == (np.size(crossed_threshold)-2):
                    crossed_and_reversed = np.append(crossed_and_reversed,crossed_threshold[i+1])
    
    return crossed_and_reversed