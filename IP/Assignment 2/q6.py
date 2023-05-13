file = open("IPmarks.txt", "r")
r = file.readlines()
#print(r)
n = int(input("Enter total no. of students : ")) #4

wts = [(10, 5), (20, 5), (100, 15), (40, 10), (100, 15),
       (20, 5), (10, 5), (40, 10), (100, 20), (50, 10)]

for i in range(n):
    a = (r[i][4:]).split(",")
    for j in range(len(a)):
        a[j] = float(a[j])
    print(a)
    sum = 0
    total_marks = 0
    weighted_list = []
    for j in range(len(wts)):
        weighted_marks = a[j]*(wts[j][1]/wts[j][0])
        weighted_list.append(round(weighted_marks, 3))
        sum += weighted_marks
        total_marks += wts[j][0]

    if sum > 80:
        grade = 'A'
    elif sum > 70:
        grade = 'A-'
    elif sum > 60:
        grade = 'B'
    elif sum > 50:
        grade = 'B-'
    elif sum > 40:
        grade = 'C'
    elif sum > 35:
        grade = 'C-'
    elif sum > 30:
        grade = 'D'
    else:
        grade = 'F'

    print("Weighted marks list =",weighted_list)
    print("Weighted sum of marks normalized to 100 for student",
          i+1, "=", round(sum, 3))
    print("Grade obtained =",grade)
    print()
    f = open("IPgrades.txt", "a")

    l = [i+1, "%.2f" %sum, grade]
    f.write(str(l)+"\n")

f.close()

# 1,  9,18,97,34,87,19,8,39.5,99,45
# 2,  8,13,91,24,97,20,8.5,39,79,43
# 3,  4,11,61,14,57,4,3,19,49,33
