import numpy as np

def f(x):
    #Gissenger coefficients
    mu = 0.119
    nu = 0.1
    gamma = 0.9
    #Gissenger values
    Q = x[0][0]
    D = x[1][0]
    V = x[2][0]
    #Time derivatives
    dQdt = mu*Q - V*D
    dDdt = -nu*D + V*Q
    dVdt = gamma - V + Q*D
    #Enter values into vector
    func = np.array([[dQdt],[dDdt],[dVdt]])

    return func

