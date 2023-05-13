course_l = []
l = []
def valid_course(s):
    if len(s) == 11 or len(s) == 10:
        if not s[:6].isalnum() or not s[:6].isupper() and not s[:7].isalnum() or not s[:6].isupper():
            print("improper course no.")
            return False
        elif not s[:3].isalnum or not s[:4].isalnum() and not s[3:6].isdigit() or not s[4:6].isdigit():
            print("improper course no.")
            return False

        elif not int(s[7]) in (1,2,4):
            print("incorrect credit")
            return False
        elif not s[9].isalpha() or not s[9].isupper() :
            print("incorrect grade")
            return False
        else:
            return True
    else:
        print("INVALID")
        return False
        
# def valid_course(s):
#     if not len(s) == 11 or not len(s) == 10:
#         if not s[:6].isalnum() and not s[:6].isupper():
#             print("improper course no.")
#         else:
#             pass
#         if not s[7].isdigit():
#             print("incorrect credit")
#         else:
#            pass
#         if not s[9].isalpha():
#             print("incorrect grade")
#         else:
#             pass
#     else:
#         return False
#     # elif len(s) < 9 and s != '':
#     #     return False
#     return True

grade_l = {"A+": 10, 'A': 10, 'A-': 9, 'B': 8,
           'B-': 7, 'C': 6, 'C-': 5, 'D': 4, 'F': 2}
while 1:
    s = input()
    if s == "":
        break
    else:
        pass

    if not valid_course(s):
        continue
        
    else:
        course_l.append(s)

    total_credits = 0
    sum = 0
    sgpa = 0
    for i in course_l:
        course_no = i[:6]
        credits = int(i[7])
        grade = int(grade_l[i[9:]])
        total_credits += (credits)
        sum += (credits*grade)

        sgpa = sum/total_credits
    l.append([s, grade])
    print('GRADE = ', grade, 'CREDITS = ', credits)
    print()

# print(l)
print("TRANSCRIPT FOR THE SEMESTER = ")
# sorted_list = sorted(l, key=lambda x: x[0][3:])  
# print(sorted_list)

courses = l
courses.sort(key=lambda x: x[0]) #sorted by the course_no 
print(courses)

for i, j in l:
    print(i[:6], ':', i[9:])
print('SGPA = ', sgpa)

# CSE101 4 A, ECE100 2 B, CSSS21 4 A-
