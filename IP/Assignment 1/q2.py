M=int(input("Enter M : "))

max_tables=50 #50=max no of tables acc. to the given eqns
max_chairs=200 #200=max no of chairs acc. to the given eqns

def maxprofit(M): #M=no of units
    x1=0  #no of tables=x1
    x2=0  #no of chairs=x2
    maxprofit=0
    for i in range(max_tables+1): 
        for j in range(max_chairs+1): 
            if i<=M:  
                price_x1=90 #profit per unit
            else:
                price_x1=100
            if j <= M:
                price_x2=25
            else:
                price_x2=30

            profit = price_x1*i + price_x2*j
            
            if 8*i+2*j<=400 and 2*i+j<=120 and profit>maxprofit:
                maxprofit=profit
                x1=i 
                x2=j
    print("Maximum profit: ",maxprofit)
    print("No. of tables to be produced daily to realize maximum profit: ",x1)
    print("No. of chairs to be produced daily to realize maximum profit: ",x2)

maxprofit(M)