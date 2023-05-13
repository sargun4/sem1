x0 =float(input("Enter value of x0 : "))

def f(x):
    return x**3 - 10.5*x**2 + 34.5*x - 35 

def derivative(x):
    return 3 * x**2 - 21*x+34.5
  
def pos_func(a): #converts -ve to +ve taking a func as argument
    if a <= 0:
        return a*(-1)
    return a*1
    
def newtonraphson(x):
    g=f(x)/derivative(x)
    while pos_func(g)>=0.01:
        g=f(x)/derivative(x)   
        x=x-g
    print("The value of the root closest to x0 is : ",round(x,2))

newtonraphson(x0)


