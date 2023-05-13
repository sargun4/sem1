import math

def sin(x):
    sinx=0
    sign=1
    for i in range(45):
        y=x*(3.14/180) #converting degrees(x) to radians(y)
        sinx+=(sign*(y**(2*i+1))/math.factorial(2*i+1))
        sign=-sign
    return sinx

def cos(x):
    cosx=1
    sign=1
    for i in range(0, 45, 2): #correction-indexing starts frm 0 not 2
        y=x*(3.14/180)
        cosx+=(sign*(y**i))/math.factorial(i)
        sign=-sign
    return cosx

angle=float(input("Enter the angle of elevation of the top of the pole = "))
d=int(input("Enter the horizontal distance from person to base of the pole = "))
l=d/cos(angle)
print("Length of the line from the person to the top of the pole = ",round(l,2))
h=sin(angle)*l
print("Height of the pole = ",round(h,2))
