import math 

a=int(input("Enter starting time = "))
b=int(input("Enter ending time = "))

def vel(t):
    vel=2000*(math.log(140000/(140000-2100*t)))-9.8*t
    return vel

while(b>a):
    dist=0
    delta_t=0.25
    dist+=((vel(a)+vel(a+delta_t))/2)*delta_t
    a+=delta_t

print("Distance covered by rocket between starting time and ending time = ",round(dist,2))

