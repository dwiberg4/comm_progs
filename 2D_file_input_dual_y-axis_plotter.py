# This is a program to Plot 2D data with 2 separate y-axes. It also has the 
# capability of putting all series labels from both y-axes into the same
# legend.

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:06:53 2020

@author: Dallin
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Times New Roman"


"""________________________________________________________________________"""
# CREATE ARRAYS FOR PLOTTIN DATA
load = open("4.4_t1_timein.txt", "r")
ld = load.readlines()
size = len(ld)
print(size)
l = []
for i in range(size):
    inter = float(ld[i])
    l.append(inter)
output1 = open("4.4_t1_posout.txt", "r")
op = output1.readlines()
size = len(op)
print(size)
o = []
for i in range(size):
    inter = float(op[i])
    o.append(inter)

output2 = open("4.4_t1_accout.txt", "r")
op2 = output2.readlines()
size = len(op)
print(size)
o2 = []
for i in range(size):
    inter = float(op2[i])
    o2.append(inter)

# CREATE THE DUAL AXIS PLOT
fig, ax1 = plt.subplots()

ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Position [m]')
lns1 = ax1.plot(l,o,label='Position',color = 'red')
ax1.tick_params(axis='y',labelcolor = 'red')

ax2 = ax1.twinx()   #instantiate a second set of axes that shares the same x-axis

ax2.set_ylabel('Acceleration [m/s^2]')
lns2 = ax2.plot(l,o2,label='Acceleration',color = 'blue')
ax2.tick_params(axis='y',labelcolor = 'blue')
# In order to put both series labels in the same legend:
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)

fig.tight_layout()

plt.show()