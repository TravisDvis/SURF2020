import math
import numpy as np

from PredictionFunctions import *

def predictReversal(xMatrix,threshold):
    
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    for kk in range(np.size(xMatrix,1)):
        
        if xMatrix[1][kk] >= 0:
            result = positiveToNegative(kk,xMatrix,threshold)
        elif xMatrix[1][kk] < 0:
            result = negativeToPositive(kk,xMatrix,threshold)
        
        if result == 0:
            true_positive = true_positive + 1
        elif result == 1:
            true_negative = true_negative + 1
        elif result == 2:
            false_positive = false_positive + 1
        elif result == 3:
            false_negative = false_negative + 1
    
    acc = (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative)
    
    f1 = (2*true_positive)/(2*true_positive + false_positive + false_negative)

    csi = (true_positive)/(true_positive + false_positive + false_negative)

    mcc_num = ((true_positive*true_negative)-(false_positive*false_negative))
    mcc_den = math.sqrt((true_positive + false_positive)*(true_positive + false_negative)*(true_negative + false_positive)*(true_negative + false_negative))
    mcc = mcc_num/mcc_den

    print("Accuracy: ",acc)
    print("F1: ",f1)
    print("Critical Success Index: ",csi)
    print("Matthew's Correlation Coefficient: ",mcc)

    skill_scores = np.array([[acc],[f1],[csi],[mcc]])

    return skill_scores
