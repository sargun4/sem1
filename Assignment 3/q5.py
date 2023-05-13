cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
policy = [80, 65, 50, 40, 30]

with open('q5.txt','r') as f:
    r = f.readlines()
    # print(r)

marks_l = []
lst_marksnrno=[]
for i in r:
    total_marks = 0
    i = (i[:-1])
    i = i.split(', ')
    rno=i[0]
    # i=(i[:-1])
    for x in i[1:]:
        x = float(x)
        total_marks += x
    print(i[1:])
    lst_marksnrno.append([rno,total_marks])
    print(total_marks)
    marks_l.append(total_marks)
    
marks_l.sort(reverse=True)
print(marks_l)

lst_marksnrno.sort(key=lambda x: x[1], reverse=True)
print(lst_marksnrno)
        

Actr=0
Bctr=0
Cctr=0
Dctr=0
Fctr=0
Agraders=[]
Bgraders=[]
Cgraders=[]
Dgraders=[]
Fgraders=[]

size=len(marks_l)
for i in range(size):
    if total_marks >= policy[0]:
        grade = "A"
    elif total_marks >= policy[1]:
        grade = "B"
    elif total_marks >= policy[2]:
        grade = "C"
    elif total_marks >= policy[3]:
        grade = "D"
    else:
        grade = "F"
        
final_cutoffs = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0} 
print()
for i in range(len(policy)):
    temp = []
    for j in marks_l:
        if j <= policy[i]+2 and j >= policy[i]-2:
            temp.append(j)
            print(temp)
            if len(temp)==1:

                if 78<=temp[0]<=82:
                    final_cutoffs['A']=temp[0] 
                elif 63<=temp[0]<=67:
                    final_cutoffs['B']=temp[0] 
                elif 48<=temp[0]<=52:
                    final_cutoffs['C']=temp[0] 
                elif 38<=temp[0]<=42:
                    final_cutoffs['D']=temp[0] 
                elif temp[0]<=40:
                    final_cutoffs['F']=temp[0]
                    
    if len(temp)==1:
        # temp[0]=j
        continue

    a = None
    b = None
    maxdiff = 0
    prev_elmnt = temp[0]
    print("temp lists=",temp)
    # print(prev_elmnt)
    for j in temp:
        if prev_elmnt-j > maxdiff:
            maxdiff = prev_elmnt-j
            a = prev_elmnt
            b = j
        prev_elmnt = j
    policy[i] = (float(a)+float(b))/2
    cutoff_val=policy[i]
    
    print(cutoff_val)
    
    if 78<=cutoff_val<=82:
        final_cutoffs['A']=cutoff_val 
    elif 63<=cutoff_val<=67:
        final_cutoffs['B']=cutoff_val 
    elif 48<=cutoff_val<=52:
        final_cutoffs['C']=cutoff_val 
    elif 38<=cutoff_val<=42:
        final_cutoffs['D']=cutoff_val 
    elif cutoff_val<=40:
        final_cutoffs['F']=cutoff_val

print("Final cutoffs dictionary =",final_cutoffs) 
print("Updated policy based on final cutoffs =",policy)

for i in range(size):
    if lst_marksnrno[i][1]>=final_cutoffs['A']:
        Agraders.append(lst_marksnrno[i][1])
    elif final_cutoffs['A']>=lst_marksnrno[i][1]>=final_cutoffs['B']:
        Bgraders.append(lst_marksnrno[i][1])
    elif final_cutoffs['B']>=lst_marksnrno[i][1]>=final_cutoffs['C']:
        Cgraders.append(lst_marksnrno[i][1])
    elif final_cutoffs['C']>=lst_marksnrno[i][1]>=final_cutoffs['D']:
        Dgraders.append(lst_marksnrno[i][1])
    elif final_cutoffs['D']>=lst_marksnrno[i][1]>=final_cutoffs['F']:
        Fgraders.append(lst_marksnrno[i][1])

    Actr=len(Agraders)
    Bctr=len(Bgraders)
    Cctr=len(Cgraders)
    Dctr=len(Dgraders)
    Fctr=len(Fgraders)
print(Agraders)
print(Bgraders)
print(Cgraders)
print(Dgraders)
print(Fgraders)
for i in range(len(lst_marksnrno)):
    tot_marks=lst_marksnrno[i][1]
    if tot_marks in Agraders:
        lst_marksnrno[i].append('A')
    elif tot_marks in Bgraders:
        lst_marksnrno[i].append('B')
    elif tot_marks in Cgraders:
        lst_marksnrno[i].append('C')
    elif tot_marks in Dgraders:
        lst_marksnrno[i].append('D')
    elif tot_marks in Fgraders:
        lst_marksnrno[i].append('F')

print(lst_marksnrno)

# print("Final cutoffs dictionary =",final_cutoffs)
print("FOR PROF = ")
print("1. Generate a summary-course info (name, credits), assessments and their weight, cutoffs for different grades, and grading summary")
print('2. Print the grades of all the students in a file as: rollno, total marks, grade')
print('3. Search for a student record - given the roll no, show marks in different assessments, total marks, and final grade')


a=input("Hey prof! What do you need? ")
print()
if a=='1':
    print(cname,credits)
    for ctr,i in enumerate(assessments):
        print(ctr+1,"-",i[0],i[1])
    # print("Final cutoffs dictionary =",final_cutoffs)
    print('----GRADING SUMMARY----')
    print('No. of As =',Actr)
    print('No. of Bs =',Bctr)
    print('No. of Cs =',Cctr)
    print('No. of Ds =',Dctr)
    print('No. of Fs =',Fctr)
elif a=='2':
    with open('q5_out.txt','w') as f:
        for i in range(len(lst_marksnrno)):
            tot_marks=lst_marksnrno[i][1]
            if tot_marks in Agraders:
                lst_marksnrno[i].append('A')
            elif tot_marks in Bgraders:
                lst_marksnrno[i].append('B')
            elif tot_marks in Cgraders:
                lst_marksnrno[i].append('C')
            elif tot_marks in Dgraders:
                lst_marksnrno[i].append('D')
            elif tot_marks in Fgraders:
                lst_marksnrno[i].append('F')
        # print(lst_marksnrno)
            f.writelines(str(lst_marksnrno[i][0])+", "+str(tot_marks)+", "+str(lst_marksnrno[i][2])+'\n')

        print("GRADES STORED IN q5_out.txt")

elif a=='3':
    rno=(input('Enter roll no of student ='))
    for i in r:
        total_marks=0
        i = (i[:-1])
        i=i.split(", ")
        for x in i[1:]:
            x = float(x)
            total_marks += x
        if i[0]==rno:
            print("Roll no. =",i[0])
            # print(i[0],i[1:],total_marks,dograding(total_marks))
            for ctr,x in enumerate(assessments):
                print(ctr+1,x[0],'=',i[ctr+1])
            print("Total marks =", total_marks)
        # grade=None
        for i in range(len(lst_marksnrno)):
            
            if rno==lst_marksnrno[i][0]:
                grade=lst_marksnrno[i][2]

    print("Grade obtained =",grade)
            
           
#  print("Final grade",dograding(total_marks))

print("-----END-----")
        