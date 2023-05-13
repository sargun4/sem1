menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70),
        ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
d = dict(menu)
print(d)
print("------CANTEEN MENU------")
print()
for index, (key, val) in enumerate(d.items()):
    print(index+1, key, val)


print()
qty = {'Samosa': 0, 'Idli': 0, "Maggie": 0, "Dosa": 0,
       "Tea": 0, "Coffee": 0, "Sandwich": 0, "ColdDrink": 0} #dict to store qty of each item ordered
print("PLACE YOUR ORDER = ")
print("Enter item number and quantity : ")
while 1:
    l = input()
    if l == "":  #pressed enter
        print("------END OF ORDER-------")
        break
    else:
        pass

    l = [int(i) for i in l.split()]
    l[0] -= 1  
    qty[menu[l[0]][0]] += l[1] #updating qty dictionary; l[1] is quantity and l[0] is item no.
    print("Order more : ")

print()
totalsum = 0
totalqty = 0
print('------BILL------')
for i, j in qty.items():

    if j != 0:
        cost = d[i]
        print(i, ",", j, ",", j*cost)
        totalsum += j*cost
        totalqty += j
print("TOTAL,", totalqty, "items, Rs", totalsum)
