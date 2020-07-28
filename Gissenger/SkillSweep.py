import numpy as np

from PredictReversal import *

def skill_sweep(xMatrix):
    
    sweep_parameter = 100
    for i in range(sweep_parameter):
        mcc = predictReversal(xMatrix,i/sweep_parameter)