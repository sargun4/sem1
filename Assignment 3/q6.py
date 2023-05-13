#  using dict method
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
            f.writelines(str([lst_marksnrno[i][0],tot_marks,lst_marksnrno[i][2]])+'\n')

        print("GRADES STORED IN q5_out.txt")

elif a=='3':
    rno=(input('Enter roll no of student ='))
    a=0
    for i in r:
        total_marks=0
        i = (i[:-1])
        i=i.split(", ")
        for x in i[1:]:
            x = float(x)
            total_marks += x
        if i[0]==rno:
            a=1
            print("Roll no. =",i[0])
            # print(i[0],i[1:],total_marks,dograding(total_marks))
            for ctr,x in enumerate(assessments):
                print(ctr+1,x[0],'=',i[ctr+1])
            print("Total marks =", total_marks)
        # grade=None
            for i in range(len(lst_marksnrno)):
                
                if rno==lst_marksnrno[i][0]:
                    grade=lst_marksnrno[i][2]
            break
    if a==1:
        print("Grade obtained =",grade)
        pass
    
    else:
        print("Roll no isnt there in existing records")   
#  print("Final grade",dograding(total_marks))

print("-----END-----")
        


import time
N=1000
if a=='2':
    start_time = time.time()
    for i in range(N):
        with open('q6new.txt','r') as file:
            r = file.readlines()

    end_time = time.time()
    time_d1 = end_time - start_time
    print("Time for grading by using dict=",time_d1)

if a=='3':
    start_time = time.time()
    for i in range(N):
            with open('q6new.txt','r') as file:
                r = file.readlines()
    end_time = time.time()
    time_d2=end_time-start_time
    print("Time for searching by using dict=",time_d2)






#using OOPS
class Course:
    def __init__(self, course_name, credits, assessments, policy):
        self.course_name = course_name
        self.credits = credits
        self.assessments = assessments
        self.policy = policy
        self.final_cutoffs = {}
        self.Actr = 0
        self.Bctr = 0
        self.Cctr = 0
        self.Dctr = 0
        self.Fctr = 0
        self.marks_l = []
        self.Agraders=[]
        self.Bgraders=[]
        self.Cgraders=[]
        self.Dgraders=[]
        self.Fgraders=[]

    def midpt_maxdiff(self, lst):
        minL = min(lst)
        maxL = max(lst)
        return (minL + maxL) / 2

    def dograding(self,marks):
        global grade
        if marks > self.policy[0]:
            grade = 'A'
            self.Actr+=1
        elif marks > self.policy[1]:
            grade = 'B'
            self.Bctr+=1
        elif marks > self.policy[2]:
            grade = 'C'
            self.Cctr+=1
        elif marks > self.policy[3]:
            grade = 'D'
            self.Dctr+=1
        elif marks < 30:
            grade = 'F'
            self.Fctr+=1
        return(grade)

    def grader(self,filename):    
        marks_l = []
        with open('q6new.txt','r') as f:
            r = f.readlines()
            # print(r)
        for i in r:
            marks = 0
            i = (i[:-1])
            i = i.split(', ')
            # print(i)
            # i=(i[:-1])
            for x in i[1:]:
                print(x)
                x = float(x)
                marks += x
            print(i[1:])
            print(marks)
            marks_l.append(marks)
            print("Grade obtained= ",self.dograding(marks))
        marks_l.sort(reverse=True)

        print(marks_l)
        size=len(marks_l)
        for i in range(size):
            if 78<=marks_l[i]<=82:  
                self.Agraders.append(marks_l[i])
                # print(Agraders)
            elif 63<=marks_l[i]<=67:
                self.Bgraders.append(marks_l[i])
                # print(Bgraders)
            elif 48<=marks_l[i]<=52:
                self.Cgraders.append(marks_l[i])
                # print(Cgraders)
            elif 38<=marks_l[i]<=42:
                self.Dgraders.append(marks_l[i])
                # print(Dgraders)
            elif 28<=marks_l[i]<=32:
                self.Fgraders.append(marks_l[i])
                # print(Fgraders)

    def listprint(self,l):
        if len(l)>0:
            return (l)
    #ONLY for calculating cutoofs
    def calc_cutoffs(self):
        print("A's cutoff lst=",self.listprint(self.Agraders))
        print("B's cutoff lst=",self.listprint(self.Bgraders))
        print("C's cutoff lst=",self.listprint(self.Cgraders))
        print("D's cutoff lst=",self.listprint(self.Dgraders))
        print("F's cutoff lst=",self.listprint(self.Fgraders))

        self.final_cutoffs={}
        self.final_cutoffs['A']=self.midpt_maxdiff(self.Agraders)
        self.final_cutoffs['B']=self.midpt_maxdiff(self.Bgraders)
        self.final_cutoffs['C']=self.midpt_maxdiff(self.Cgraders)
        self.final_cutoffs['D']=self.midpt_maxdiff(self.Dgraders)
        self.final_cutoffs['F']=self.midpt_maxdiff(self.Fgraders)

    

    print("FOR PROF = ")
    print("1. Generate a summary-course info (name, credits), assessments and their weight, cutoffs for different grades, and grading summary")
    print('2. Print the grades of all the students in a file as: rollno, total marks, grade')
    print('3. Search for a student record - given the roll no, show marks in different assessments, total marks, and final grade')

    def Prof(self,fname):
        global a
        # a=input("Hey prof! wdu need? ")
        print()
        if a=='1':
            print(cname,credits)
            for ctr,i in enumerate(self.assessments):
                print(ctr+1,"-",i[0],i[1])
            print("Final cutoffs dictionary =",self.final_cutoffs)
            print('----GRADING SUMMARY----')
            print('No. of As =',self.Actr)
            print('No. of Bs =',self.Bctr)
            print('No. of Cs =',self.Cctr)
            print('No. of Ds =',self.Dctr)
            print('No. of Fs =',self.Fctr)
        elif a=='2':
            with open(fname,'r') as file:
                r = file.readlines()
            with open('q6out','w') as f:
                for i in r:
                    marks=0
                    i = (i[:-1])
                    i=i.split(", ")
                    for x in i[1:]:
                        x = float(x)
                        marks += x
                    f.writelines(str([i[0],marks,(self.dograding(marks))])+'\n')
            print("GRADES STORED IN q6out.txt")
        elif a=='3':
            rno=(input('Enter roll no of student ='))
            with open('q6new.txt','r') as file:
                r = file.readlines()
            for i in r:
            
                marks=0
                i = (i[:-1])
                i=i.split(", ")
                for x in i[1:]:
                    x = float(x)
                    marks += x
                if i[0]==rno:
                    print("Roll no. =",i[0])
                    # print(i[0],i[1:],marks,dograding(marks))
                    for ctr,x in enumerate(self.assessments):
                        print(ctr+1,x[0],i[ctr+1])
                    print("Total marks =", marks)
                    print("Final grade",self.dograding(marks))
        print("-----END-----")
        

cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
policy = [80, 65, 50, 40, 30]
# course = Course(cname, credits, assessments, policy)
# course.grader('q4.txt')
# course.Prof('q4.txt')
# print("Final cutoffs dictionary =",final_cutoffs)
q6ops = Course(cname, credits, assessments, policy)
q6ops.grader('q6new.txt')
q6ops.Prof('q6new.txt')


import time
N=1000
if a=='2':
    start_time = time.time()
    for i in range(N):
        with open('q6new.txt','r') as file:
            r = file.readlines()

    end_time = time.time()
    time_oo1 = end_time - start_time
    print("Time for grading by using OOPS=",time_oo1)

if a=='3':
    start_time = time.time()
    for i in range(N):
            with open('q6new.txt','r') as file:
                r = file.readlines()
    end_time = time.time()
    time_oo2=end_time-start_time
    print("Time for searching by using OOPS=",time_oo2)


#COMPARISON
#for GRADING
if a=='2':
    with open('q6out.txt','a') as f:
        if time_oo1 < time_d1:
            faster = "OO"
            fraction = time_oo1 / time_d1
        else:
            faster = "Dictionary"
            fraction = time_d1 / time_oo1

        f.write("\nPerformance comparison for grading operation:\n")
        f.write("N: {}\n".format(N))
        f.write("Time by OO: {}\n".format(time_oo1))
        f.write("Time by Dictionary: {}\n".format(time_d1))
        f.write(str("{} is faster; fraction of time {} took is: {}".format(faster, faster, fraction)+'\n'))


    print("Performance comparison for grading operation:")
    print("N:", N)
    print("Time by OO:", time_oo1)
    print("Time by Dictionary:", time_d1)
    print(faster, "is faster; fraction of time", faster, "took is:", fraction,'\n')
    

#for SEARCHIN
if a=='3':
    if time_oo2 < time_d2:
        faster = "OO"
        fraction = time_oo2 / time_d2
    else:
        faster = "Dictionary"
        fraction = time_d2 / time_oo2

    print("\nPerformance comparison for search operation:")
    print("N:", N)
    print("Time by OO:", time_oo2)
    print("Time by Dictionary:", time_d2)
    print(faster, "is faster; fraction of time", faster, "took is:", fraction,'\n')


    with open('q6out.txt','a') as f:
        if time_oo2 < time_d2:
            faster = "OO"
            fraction = time_oo2 / time_d2
        else:
            faster = "Dictionary"
            fraction = time_d2 / time_oo2
        f.write("Performance comparison for search operation:\n")
        f.write("N: {}\n".format(N))
        f.write("Time by OO: {}\n".format(time_oo2))
        f.write("Time by Dictionary: {}\n".format(time_d2))
        f.write("{} is faster; fraction of time {} took is: {}".format(faster, faster, fraction),'\n')