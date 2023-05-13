class Course:
    grades = ["A", "B", "C", "D", "F"]

    def __init__(self, course_name, credits, assessments, policy):
        self.course_name = course_name #IP
        self.credits = credits #4
        self.assessments = assessments
        # [("quiz", 15), ("midsem", 30), ("lab", 15), ("endsem", 40)]
        self.policy = policy
        self.students = [] #lsit storing stud records

    def student_record(self, course_name, rno, assessment_marks):
        total_marks = 0
        for mark in assessment_marks:
            total_marks += mark[1]
             # addin studt record to students list
        self.students.append(Student(course_name, rno, assessment_marks, total_marks))

    def grade_students(self):
        for student in self.students:
            #self.policy=[80, 65, 50, 40]
            if student.total_marks >= self.policy[0]:#80
                student.grade = self.grades[0]#A
            elif student.total_marks >= self.policy[1]:#65
                student.grade = self.grades[1]#B
            elif student.total_marks >= self.policy[2]:#50
                student.grade = self.grades[2]#C
            elif student.total_marks >= self.policy[3]:#40
                student.grade = self.grades[3]#D
            else:
                student.grade = self.grades[4]#F
                
    def update_policy(self):
        marks_list = [] # list to store total marks of all students
        for student in self.students:
            marks_list.append(student.total_marks)

        marks_list.sort(reverse=True)
        
    
        global final_cutoffs
        #storing each grade's fin cutoof 
        final_cutoffs = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0} 

        for i in range(len(self.policy)):
            temp = []
            for j in marks_list:
                 # checking if marks is within +/- 2 of policy mrking
                if j <= self.policy[i]+2 and j >= self.policy[i]-2:
                    temp.append(j)
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
                continue
            """final cutoff for each grade will be within +/- 2 of the percent specified (i.e. for A it will be between 78 and 82) - it will be the midpt of two consecutive marks within this range which have the highest difference."""
        # to calc finalcutoff based on highest gap bw two consec. marks 
            print(temp)
            a = None
            b = None
            diff = 0
            prev = temp[0]
            # print(prev)

            for j in temp:
                if prev-j > diff:
                    diff = prev-j
                    a = prev
                    b = j
                prev = j
            self.policy[i] = (a+b)/2
            cutoff_val=self.policy[i]
            print(cutoff_val)
            
            if 78<=cutoff_val<=82:
                final_cutoffs['A']=cutoff_val 
            elif 63<=cutoff_val<=67:
                final_cutoffs['B']=cutoff_val 
            elif 48<=cutoff_val<=52:
                final_cutoffs['C']=cutoff_val 
            elif 38<=cutoff_val<=42:
                final_cutoffs['D']=cutoff_val 
            elif cutoff_val<40:
                final_cutoffs['F']=cutoff_val

        # print("Final cutoffs dictionary =",final_cutoffs) 
        # print("Updated policy based on final cutoffs =",policy)

 
    def gradesummary(self):
        Actr = 0 #ctrs to track each grade no.
        Bctr = 0
        Cctr = 0
        Dctr = 0
        Fctr = 0
        for studnt in self.students:
            if studnt.grade == self.grades[0]:#A
                Actr+=1
            if studnt.grade == self.grades[1]:#B
                Bctr+=1
            if studnt.grade == self.grades[2]:
                Cctr+=1
            if studnt.grade == self.grades[3]:
                Dctr+=1
            if studnt.grade == self.grades[4]:#F
                Fctr+=1
        print("No. of A's :", Actr)
        print("No. of B's :", Bctr)
        print("No. of 'C's :", Cctr)
        print("No. of D's :", Dctr)
        print("No. of F's :", Fctr)
        
class Student:
    def __init__(self, course_name, rno, assessments_marks, total_marks):
        self.course_name = course_name
        self.rno = rno
        self.total_marks = total_marks
        self.assessments_marks = assessments_marks


policy =  [80, 65, 50, 40] 
assessments = [("quiz", 15), ("midsem", 30), ("lab", 15), ("endsem", 40)]
course = Course("IP", 4, assessments, policy)

with open("q4.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        temp = [["quiz", 0], ["midsem", 0], ["lab", 0], ["endsem", 0]]
        i = i.split(",")
        i[-1] = i[-1][:-1]
        for j in range(len(i)):
            if j==0:
                pass
            elif j==1:
                i[j] = int(i[j])
            else:
                i[j] = float(i[j])
        for j in range(len(temp)):
            temp[j][1] = i[j+2]
        course.student_record(i[0], i[1], temp)

course.update_policy()
course.grade_students()

print("FOR PROF = ")
print("1. Generate a summary-course info (name, credits), assessments and their weight, cutoffs for different grades, and grading summary")
print('2. Print the grades of all the students in a file as: rollno, total marks, grade')
print('3. Search for a student record - given the roll no, show marks in different assessments, total marks, and final grade')

while True:
    x=input("Hey prof! What do you need? ")
    if x=='':
        print("User pressed enter")
        break
    elif x== '1':
        print(course.course_name, course.credits)
        # print(course.assessments)
        # print("final cutoffs dict =",course.policy)
        
        # print(cname,credits)
        
        for ctr,i in enumerate(course.assessments):
            print(ctr+1,"-",i[0],i[1])
        print('----GRADING SUMMARY----')
        course.gradesummary()
     
        # print('No. of As =',Actr)
        # print('No. of Bs =',Bctr)
        # print('No. of Cs =',Cctr)
        # print('No. of Ds =',Dctr)
        # print('No. of Fs =',Fctr)
    elif x== '2':
        with open("q4-out.txt", "w") as file:
                for studnt in course.students:
                    print(studnt.course_name+", "+str(studnt.rno)+", "+str(studnt.total_marks)+", "+studnt.grade)
                    file.write(studnt.course_name+", "+str(studnt.rno)+", "+str(studnt.total_marks)+", "+studnt.grade+"\n")

    elif x== '3':
        rno = int(input("type the rollNo: "))
        a=0
        for studnt in course.students:
            if studnt.rno == rno:
                a=1
                print(studnt.course_name, studnt.rno, studnt.total_marks, studnt.grade)
                break
            else:
                a=0
        if a==1:
            pass
        else:
            print("Roll no isnt there in existing records")
    else:
        break
