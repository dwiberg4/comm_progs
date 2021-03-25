# Program to perform SSE with internal array of data points
# NO File import.

import numpy as np


"""________________________________________________________________________"""
# create arrays for calibration data

#l = [14.8,18.5,22.2]
#o = [1200,1800,2400]
#l = [1,2,3,4,5,6,7,8,9,10,11,12,13.2]
#o = [41,80,128,163,202,235,262,300,336,353,383,400,428]
#l = [1,2,3,4,5,6,7,8,9,10,11,12,13.6]
#o = [44,83,126,168,195,226,250,272,295,330,366,386,430]
#l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#o = [39,73,101,136,160,188,210,230,247,266,290,315,346]
#l = [14.8,18.5,22.2]
#o = [.4352941176,.37,.32647]

#l = [1775,574,902,1600,192,842,752,1080,850,450,420,1360,831,423,1690,477,1366,580,482,498,598,523,452,318,324]
#o = [20000,5000,10000,22000,1550,10000,8000,12000,11000,5200,4500,16000,8000,5200,22000,5000,16000,6200,5000,5000,6600,6500,4500,3300,3000]
l = [575,976,360,677,228,538,590,405,620,565,318,232,590]
o = [5000,6200,3000,5000,1500,4000,5000,3250,5000,5000,2200,1500,5000]
l = [75,150,225,300]
o = [340,550,620,740]
l = [10,15,20,25,30,35]
o = [0.557159499315788,0.53546858700653,0.552167268083489,0.578337352857883,0.600983086105154,0.621180528094503]
l = [10,15,20,25,30,35]
o = [0.32790189626285,0.318019806936888,0.310330997164903,0.309111528062725,0.305979182855263,0.317063899914052]
l = [0.1,0.4,0.7,1.0]
o = [1.5,6.0,10.5,15]
l = [-0.16,-0.06,0.13,0.35,0.54,0.76,0.99,1.18,1.41,1.64,1.94]
o = [0.2,0.48,1.4,2.35,3.35,4.8,5.35,6.3,7.35,8.4,9.8]



size = len(l)



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
print()

    












