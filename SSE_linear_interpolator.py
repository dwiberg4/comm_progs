# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:09:09 2020

@author: Dallin
"""

import numpy as np


"""________________________________________________________________________"""
# create arrays for calibration data
# copy and paste this path: C:\Users\Dallin\Documents\USU 2020 aSpring\Instr. & Meas\LAB 5
path = input("Please enter the file path.")
fl = "\cal_temp.txt"
path2 = path+fl

load = open(path2, "r")
ld = load.readlines()
#print(ld)
size = len(ld)
print(size)
l = []
for i in range(size):
    inter = float(ld[i])
    l.append(inter)
print(l)

fl2 = "\cal_volt.txt"
path3 = path+fl2
output = open(path3, "r")
op = output.readlines()
#print(op)
size = len(op)
print(size)
o = []
for i in range(size):
    inter = float(op[i])
    o.append(inter)
print(o)

# Now perform the SSE functions with the arrays
xsum = ysum = xysum = x2sum = 0
for i in range(size):
    xsum += l[i]
    ysum += o[i]
    xysum += (l[i]*o[i])
    x2sum += (l[i]*l[i])
xsum2 = (xsum**2)
print("xsum: ",xsum)
print("ysum: ",ysum)
print("xysum: ",xysum)
print("x2sum: ",x2sum)
print("xsum2: ",xsum2)

A = ((xysum-((1/size)*xsum*ysum))/ (x2sum-((1/size)*xsum2)))
print("A: ",A)
B = (((1/size)*ysum)- ((A*(1/size)*xsum)))
print("B: ",B)

# produce the interpolation function
def interp(x):
    y = (A*x) + B
    return y

# run a check on the interpolation equation and on the goodness of the data
y = []
diffs = []
for i in range(size):
    y.append(interp(l[i]))
    diffs.append(abs(y[i]-o[i]))

print("Interpolated y values are: \n",y)
print("Differences between experimental and calibrated values are: \n",diffs)


# Print the Calibration Equation

print("\n\ny =",A,"\b*x +",B)

    













