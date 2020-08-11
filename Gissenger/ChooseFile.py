import numpy as np
import tkinter as tk

from tkinter import filedialog

def processFile():
    
    file_path = filedialog.askopenfilename()
    
    with open(file_path,"r") as file:

        count = 0
        data_matrix = np.array([[],[],[],[],[]])

        for i in file:
            
            line = file.readline().split(',')
        
            if line[0].isalpha() or line[0] == '':
                continue

            t = float(line[0])
            D = float(line[1])

            iteration = np.array([[0],[D],[0],[t],[count]])
            data_matrix = np.append(data_matrix,iteration,axis=1)

            count = count + 1
            
    return data_matrix