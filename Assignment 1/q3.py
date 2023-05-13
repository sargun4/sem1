x0=0
y0=0
x=x0
y=y0
totaldist=0
d=1
while(d>0):
    d=int(input())
    if d<0:
        break
    totaldist+=d
    if d<=25:
        y+=d
    elif d>=26 and d<=50:
        y-=d
    elif d>=51 and d<=75:
        x+=d
    else:
        x-=d
x0=x
y0=y  
print("Final coordinates = ","(",x,",",y,")")
print("Total distance covered = ",totaldist)
straightlinedist=(x0**2+y0**2)**0.5
print("The straight line distance covered = ",straightlinedist) 
