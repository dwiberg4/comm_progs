# A program to calculate the area of a Triangle in 3D space
# The initial input is 3, 3D coordinates


import numpy as np 

A = [4,1,3]
B = [6,6,1]
C = [-3,3,2]

#A = [0,0,0]
#B = [4,0,0]
#C = [0,3,0]

def distance_3D(A,B):
    dist = np.sqrt(   ((B[0]-A[0])**2)+((B[1]-A[1])**2)+((B[2]-A[2])**2)  )
    return dist

#print("The distance between the points A and B is: ",distance_3D(A,B))
#print("The distance between the points B and C is: ",distance_3D(B,C))
#print("The distance between the points C and A is: ",distance_3D(C,A))

def area_3D(A,B,C):
    a = distance_3D(B,C)
    b = distance_3D(C,A)
    c = distance_3D(A,B)
    angle_C = np.arccos(  (  (c**2)-(a**2)-(b**2)  )  /(-2*a*b)  )
    h = a*np.sin(angle_C)
    area = .5*b*h
    return area

def herons_area(A,B,C):
    a = distance_3D(B,C)
    b = distance_3D(C,A)
    c = distance_3D(A,B)
    s = (a+b+c)/2
    area = np.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

area = area_3D(A,B,C)
herons = herons_area(A,B,C) 
print("The area of the Triangle is: ",area)
print("According to Heron's Formula, the area of the Triangle is: ",herons)
