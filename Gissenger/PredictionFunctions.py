import math
import numpy as np


def runPrediction(xMatrix,threshold_pos,threshold_neg,reversal_times,dt):
    
    #initialize values
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    #initialize curve indicating when reversal is happening
    reversal_curve = reversalCurve(xMatrix,threshold_pos,threshold_neg,reversal_times,dt)
    #iterate through Matrix
    for kk in range(np.size(xMatrix,1)):
    #If value is below threshold, reversal prediction is affirmative
        if xMatrix[1][kk] <= threshold_pos and xMatrix[1][kk] >= -1*threshold_neg:
            reversal_prediction = True
        else:
            reversal_prediction = False
    #Compare prediction and reversal occurrences
        if reversal_prediction == True and reversal_curve[kk] == 1:
            true_positive = true_positive + 1
        elif reversal_prediction == False and reversal_curve[kk] == 0:
            true_negative = true_negative + 1
        elif reversal_prediction == True and reversal_curve[kk] == 0:
            false_positive = false_positive + 1
        elif reversal_prediction == False and reversal_curve[kk] == 1:
            false_negative = false_negative + 1
        elif reversal_curve[kk] == 2:
            continue
    #Accuracy
    acc = (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative)
    #F1 Score
    try:
        f1 = (2*true_positive)/(2*true_positive + false_positive + false_negative)
    except ZeroDivisionError:
        f1 = 0
    #Critical Success Index
    try:
        csi = (true_positive)/(true_positive + false_positive + false_negative)
    except ZeroDivisionError:
        csi = 0
    #Matthew's Correlation Coefficient
    mcc_num = ((true_positive*true_negative)-(false_positive*false_negative))
    mcc_den = math.sqrt((true_positive + false_positive)*(true_positive + false_negative)*(true_negative + false_positive)*(true_negative + false_negative))
    try:
        mcc = mcc_num/mcc_den
    except ZeroDivisionError:
        mcc = 0
    #Storing all skill scores into an array
    skill_scores = np.array([[acc],[f1],[csi],[mcc]])

    return skill_scores            


def reversalCurve(xMatrix,threshold_pos,threshold_neg,reversal_times,dt):
    
    #Intialize reversal curve
    reversal_curve = np.zeros(np.size(xMatrix,1))
    crossed_reversed = crossAndReversed(xMatrix,threshold_pos,threshold_neg,reversal_times)

    width = int(0.5/dt)

    #Iterate through matrix/reversal times and indeces
    for i in range(np.size(xMatrix,1)):
        for ii in range(np.size(crossed_reversed,0)):
            for iii in range(np.size(crossed_reversed,1)-1):
                if i == crossed_reversed[ii][iii]:
                    for iv in range(int(crossed_reversed[ii][iii]),int(crossed_reversed[ii][iii+1])):
                       for v in range(np.size(reversal_times,1)):
                            if crossed_reversed[ii][iii] <= reversal_times[1][v] and crossed_reversed[ii][iii+1] >= reversal_times[1][v]:
                                #Checkpoint
                                for vi in range(int(reversal_times[1][v])-width,int(reversal_times[1][v])):
                                    reversal_curve[vi] = 1
                                for vii in range(int(reversal_times[1][v]),int(crossed_reversed[ii][iii+1])):
                                    reversal_curve[vii] = 2
    
    return reversal_curve

def crossThreshold(xMatrix,threshold_pos,threshold_neg):
        
    crossed_threshold = np.empty([0,2])
    crossed_threshold_1 = np.array([])

    count = 0

    for kk in range(np.size(xMatrix,1)-1):
        
        if xMatrix[1][kk] > threshold_pos:
            sign_before = 0
        elif xMatrix[1][kk] < -1*threshold_neg:
            sign_before = 1
        elif xMatrix[1][kk] <= threshold_pos and xMatrix[1][kk] >= -1*threshold_neg:
            sign_before = 2

        if xMatrix[1][kk+1] > threshold_pos:
            sign_after = 3
        elif xMatrix[1][kk+1] < -1*threshold_neg:
            sign_after = 4
        elif xMatrix[1][kk+1] <= threshold_pos and xMatrix[1][kk+1] >= -1*threshold_neg:
            sign_after = 5

        if sign_before == 0 and (sign_after == 4 or sign_after == 5):
            crossed_threshold_1 = np.append(crossed_threshold_1,kk+1)
            count = count + 1
        elif sign_before == 1 and (sign_after == 3 or sign_after == 5):
            crossed_threshold_1 = np.append(crossed_threshold_1,kk+1)
            count = count + 1
        elif sign_before == 2 and (sign_after == 3 or sign_after == 4):
            crossed_threshold_1 = np.append(crossed_threshold_1,kk+1)
            count = count + 1

        if count == 2:
            count = 0
            crossed_threshold = np.append(crossed_threshold,[crossed_threshold_1],axis=0)
            crossed_threshold_1 = np.array([])

    return crossed_threshold

def crossAndReversed(xMatrix,threshold_pos,threshold_neg,reversal_times):
    
    crossed_threshold = crossThreshold(xMatrix,threshold_pos,threshold_neg)
    crossed_and_reversed = np.empty([0,2])
   
    for i in range(np.size(crossed_threshold,0)):
        for ii in range(np.size(crossed_threshold,1)-1):
            for iii in range(np.size(reversal_times,1)):
                if reversal_times[1][iii] >= crossed_threshold[i][ii] and reversal_times[1][iii] <= crossed_threshold[i][ii+1]:
                    crossed_and_reversed_1 = np.array([crossed_threshold[i][ii],crossed_threshold[i][ii+1]])
                    crossed_and_reversed = np.append(crossed_and_reversed,[crossed_and_reversed_1],axis=0)
    
    return crossed_and_reversed
