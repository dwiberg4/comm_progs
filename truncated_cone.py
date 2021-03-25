import numpy as np 



b = eval(input("Please enter the Large radius. "))
r = eval(input("Please enter the small radius. "))
h = eval(input("Please enter the height. "))

print("b,r,h are: ",b,r,h)
print(type(b))
print(type(r))
print(type(h))

def lat_area(b,r,h):
    area = (np.pi*(b+r)) * (np.sqrt(((b-r)**2)+ (h**2)))
    return area

def my_area(b,r,h):
    myarea = (np.pi*(((b**2)-(r**2))/r)) * (np.sqrt(((b-r)**2)+ (h**2)))
    return myarea
    

area = lat_area(b,r,h)
print("The lateral area of the truncated cone is: ",area)

# Let the record show, my derivation is not a general solution.
# It only works for the case of b = 20, r = 10, h = 50.....
myarea = my_area(b,r,h)
print("My equation area is equal to: ",myarea)

