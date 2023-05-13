import math
price = 1

def D(p):
    D=math.exp(10-1.05*p)
    return D

def S(p):
    S=math.exp(1+1.06*p) 
    return S

def checkeqlbrm(price):
    mindiff=D(price)-S(price)
    diff=0
    if mindiff<0:
        mindiff*(-1) # to handle cases where D(p)-S(p) is negative
    if diff<0:
        diff*(-1)
    while mindiff >= D(price)-S(price):
        diff = D(price)-S(price)
        if diff < 50:
            print("equilibrium price = ",round(price,2))
            print("demand at equilibrium price = ",round(D(price),2))
            print("supply at equilibrium price = ",round(S(price),2))
            break
        else:
            price += 0.05*price
    if diff>=mindiff:
        print("No solution possible")
checkeqlbrm(price)