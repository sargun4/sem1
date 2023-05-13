cost=int(input("Enter laptop cost = "))
allowance=20000
sf=0.1
r=0.5
savings=allowance*sf
saved=0
t=0
while(saved<cost):
    saved+=savings
    saved+=(saved*r)/100
    t+=1
print("Remaining money: ",saved-cost)
print("No of months required for buying the laptop: ",t)

