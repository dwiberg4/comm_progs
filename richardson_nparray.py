# Program to run the Richardson Extrapolation on a 3 Density study

import numpy as np 
import pandas as pd 
import json



# Define the Richardson Extrapolation Function
# Recieves 3 np.arrays and returns a single interpolated value array
def Rich_Extra(coarse,medium,fine):
    extra = np.array([])
    p_store = np.array([])
    r_21 = 2
    r_32 = 2
    for j in range(fine.size):
    #for j in range(len(size)):
        C_L1 = fine[j]
        C_L2 = medium[j]
        C_L3 = coarse[j]
        i = 1
        error = 1.
        p = 2.
        while (error > 1.0E-6 and i < 10):
            i = i + 1
            s = np.sign( (C_L3 - C_L2)/(C_L2 - C_L1) )
            q_p = np.log( (r_21**p - s)/(r_32**p - s) )
            p1 = abs( np.log( abs((C_L3 - C_L2)/(C_L2 - C_L1)) ) + q_p )/np.log(r_21)
            error = abs(p1 - p)
            p = p1
        p_store = np.append(p_store, [p])
        extra = np.append(extra, [(r_21**p * C_L1 - C_L2)/(r_21**p - 1.)])
    p_avg = np.mean(p_store)
    return extra


cor = np.array([1,2,3,4,5])
med = np.array([1.1,2.1,3.1,4.1,5.1])
fin = np.array([1.9,2.9,3.9,4.9,5.9])
extra = Rich_Extra(cor,med,fin)
print("The extra array is: ",extra)


c = np.array([0.3365280993,0.007357826227,-0.5904092564])
m = np.array([0.3191568363,0.007335419169,-0.5740076843])
f = np.array([0.3035530852,0.007316426188,-0.5575806431])

rich = Rich_Extra(c,m,f)
print("machup stuff is: ", rich)
print(rich[0])
print(rich[1])
print(rich[2])
