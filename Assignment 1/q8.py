pop = [50, 1450, 1400, 1700, 1500, 600, 1200]

def population(yr,pop):
    pop_new=pop.copy()
    prevyrpop=0    
    r=0.025
    for i in pop:
        prevyrpop+=i
    for i in range(yr):
        ctr=0
        for j in pop_new:
            prevyrpop+=j*(r-0.004*ctr)
            pop_new[ctr]+=j*(r-0.004*ctr)
            ctr += 1
        r-=0.001
        
    return prevyrpop  
             
yr_maxpop = 0

while population(yr_maxpop,pop) < population(yr_maxpop+1,pop):
    yr_maxpop+=1
    
print("the current population is =",(population(0,pop))," billion")
print("the year when the population will max is = ", yr_maxpop)
print("the max population will be = ", round(population(yr_maxpop,pop),2)," billion")
