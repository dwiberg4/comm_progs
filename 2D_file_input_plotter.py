# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:06:53 2020

@author: Dallin
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Times New Roman"


"""________________________________________________________________________"""
# create arrays for calibration data
load = open("ind_variable.txt", "r")
ld = load.readlines()
size = len(ld)
print(size)
l = []
for i in range(size):
    inter = float(ld[i])
    l.append(inter)

output = open("dep_variable.txt", "r")
op = output.readlines()
size = len(op)
print(size)
o = []
for i in range(size):
    inter = float(op[i])
    o.append(inter)
"""
#Calibration Line if desired
def calibration_line(x):
    y = 0.16883585928433661*x + 0.024978336099327647
    return y
caly = []
for i in size:
    caly.append(calibration_line(l(i)))
print("the caly array is: ",caly)
"""

# Create ALUMINIUM plot
plt.plot(l,o,label = 'Label 1 name',color = "red",linestyle = "None",marker= 'o',markersize= 4)
plt.plot(l.caly,label = 'Label 2 name', color = "blue")
plt.title("Calibration Plot")
plt.xlabel("Temperature [°C]")
plt.ylabel("Voltage [V]")

plt.show()
plt.savefig('cal_plot.png')
