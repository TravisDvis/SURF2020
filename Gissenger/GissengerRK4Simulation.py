import numpy as np
import matplotlib.pyplot as plt

from ChooseFile import *
from FloatExceptionHandle import *
from GissengerFunction import *
from ReversalTimes import *
from PlotRK4 import *
from SkillSweep import *
from mpl_toolkits import mplot3d
from RK4Scheme import *

#time/time step
dt = floatExceptionHandle('Enter time step: ',0)
T = floatExceptionHandle('Enter total time: ',1)
nSteps = int(T/dt)
#initial condition
print("Enter Initial Condition")
x0_x = floatExceptionHandle('Enter x coordinate: ',1)
x0_y = floatExceptionHandle('Enter y coordinate: ',1)
x0_z = floatExceptionHandle('Enter z coordinate: ',1)
x0 = np.array([[x0_x],[x0_y],[x0_z],[0],[0]])
#RK4 Matrix
data_matrix = processFile()
x = RK4Scheme(x0,dt,nSteps)
#reversal time vector
reversal_times = getReversalTimes(x)
#plots RK4
plotRK4(x,reversal_times)
#sweep plotting mcc vs thresholds
skillSweep(x,reversal_times,dt)