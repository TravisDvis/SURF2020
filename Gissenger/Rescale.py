import numpy as np

def rescale(xMatrix):

    while True:
        rescaled_xMatrix = np.array(xMatrix,copy=True)
        x = str(input("Do you want to rescale the dipole values? (Y/N): "))
        if x == "Y" or x == "y":
            max = np.amax(abs(rescaled_xMatrix[1][:]))
            rescaled_xMatrix[1][:] = rescaled_xMatrix[1][:]/max
            break
        elif x == "N" or x == "n":
            break                 
        else:
            print("Try again. Please enter \"Y/y\" or \"N/n.\"")
    
    return rescaled_xMatrix
    