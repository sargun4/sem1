with open("pages.txt", "r") as f:
    r = f.readlines()
ref={} #Dict with page url as key and url links that page contains as values=
d = {} #URLpage as key & init importance as val
for i in r:
    temp = i.split(",")
    temp1 = temp[1].split(":")
    temp[1] = float(temp1[0])
    temp.insert(2, temp1[1])
    d[temp[0]] = temp[1]
    #print(temp)  # list of every entry in pages.txt
    #print(temp1)
# print(r)
for i in r:
    temp = i.split(",")
    temp1 = temp[0].split(":")
    #temp[1] = float(temp1[0])
    temp[-1] = temp[-1][:-1]
    temp[1]=temp[1][7:]
    temp=[i[1:] for i in temp]
    ref[temp1[0]]=temp[1:]
# print(d)
# print(ref)
# print(ref)

imp = {} #Overall importance d 

# for i in r:
#     temp = i.split(",")
#     temp1 = temp[1].split(":")
#     temp[1] = float(temp1[0])
#     temp.insert(2, temp1[1])
#     temp[-1] = temp[-1][:-1]
#     val = 0
#     for i in set(temp[2:]):  # set for unique links
#         i = i[1:]  # since there is a space before every URL
#         val += d[i]
#     imp[temp[0]] = round(val, 1)

for i in d:
    imp[i]=0

for i in d:
    ctr=0
    for j in ref.values():
        if i in j:
            ctr+=1
    #print(ctr)
    for j in ref:
        if i in ref[j]:
            imp[j]+=((d[i]/ctr))
print("Dict with page url as key and url links that page contains as values=",ref) 
# print("Overall importance d :", imp)
print()

l = sorted(imp.items(), key=lambda item: item[1])
# list of tuples with page and its overall importance
print("Sorted list of tuples :", l)
print()
n = int(input("Enter n")) 
print("Highest ranking", n, "pages :")


if n != 10:
    for i in l[-1:10-n-1:-1]: # reversing
        print(i[0])
else:
    for i in l[-1:11-n-1:-1]:
        print(i[0])

# URL00, 0.5: URL01, URL09, URL08, URL03
# URL01, 0.6: URL05, URL04, URL00, URL05
# URL02, 0.5: URL05, URL04 
# URL03, 0.3: URL03, URL04, URL00, URL04
# URL04, 0.1: URL05, URL05, URL02, URL02
# URL05, 0.6: URL05, URL08, URL00, URL09
# URL06, 0.9: URL05, URL09, URL00, URL01
# URL07, 0.5: URL05, URL01
# URL08, 0.6: URL05, URL03, URL01
# URL09, 0.2: URL05, URL04, URL00