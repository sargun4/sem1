n = int(input("Enter total number of graduating students = "))
# yearbook = {name1: {}, name2: {}, name3:{},name4: {}, name5: {}, name6:{}}
file = open(r"C:\Users\Dell\Desktop\prog\IP\Assignment 2\q3.txt", "r")
r = file.readlines()
dict = {}  # dictionary for yearbook
ctr_list = []  # stores no. of signatures of each student
for i in range(0,(n**2-n+1), n):
    temp = {}  # acts as nested dictionary for dict-stores name and if student has signed or not
    l = []  # temporary list which stores 1's and 0's for each student for signs
    ctr = 0
    print("List of :", r[i][:-2])  # signed list for student
    for j in range(1, n):
        temp2 = r[i+j].split(",")
        # print(temp2[0]) -other students
        # storing name(temp2[0]) as key of temp & sign(temp2[1]) as val.
        temp[temp2[0]] = int(temp2[1])
    dict[r[i][:-2]] = temp

    for k in temp.keys():
        #print(temp[k], end=" ")
        l.append(temp[k])

    for i in l:
        if i == 1:
            ctr += 1
    ctr_list.append(ctr)

    print(l)

    print(ctr)
    print()

#print(dict)

# for i in dict.keys():
#     print(dict[i])
print(ctr_list)

d = {}
for i in range(0, int(n**2-n+1), n):
    #print(r[i][:-2])
    d[r[i][:-2]] = ctr_list[i//5]

val = list(d.values())

key = list(d.keys())

print("most signatures are", max(ctr_list), "in",
      (key[val.index(max(val))]), "'s yearbook.")
print("least signatures are", min(ctr_list), "in",
      (key[val.index(min(val))]), "'s yearbook.")

# maxsign=ctr_list.index(max(ctr_list))
# minsign=ctr_list.index(min(ctr_list))
# print(maxsign)
# print(minsign)

print(d)  # dict for total signs each student gets

file.close()
