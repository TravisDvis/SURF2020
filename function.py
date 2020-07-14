import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

mu = 0.119
nu = 0.1
gamma = 0.9

def f(x):

    Q = x[0][0]
    D = x[1][0]
    V = x[2][0]

    dQdt = mu*Q - V*D
    dDdt = -nu*D + V*Q
    dVdt = gamma - V + Q*D
   
    func = np.array([[dQdt],[dDdt],[dVdt]])

    return func

