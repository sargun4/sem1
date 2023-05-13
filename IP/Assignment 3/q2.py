data = {}
with open("q2.txt",'r') as f:
        r=f.readlines()
        for i in r:
            i=i.split(', ') #splitting
            i[-1]=i[-1][:-1] # remove the \n char from the last item
            name, crossing, gate_no, time = i # Unpack the values into separate variables

            # If the name already exists in the dictionary, append the new data to the existing list of dictionaries
            if name in data:
                data[name].append({"crossing": crossing, "Gate number": gate_no, "Time": time})
            else:
                data[name] = [{"crossing": crossing, "Gate number": gate_no, "Time": time}]
# print(data)

#1. check if a student is currently present in the campus
def check_presence(name, current_time):

    """student_time = data[name][-1]["Time"] # get most recent time for student

    # Check if the current time is greater than the most recent time the student was seen    
    if current_time > student_time:
        print(f"{name} is currently in the campus")
    else:
        print(f"{name} is not currently in the campus")

    with open("studentrecord.txt",'w') as f:
        f.write(str(name)+'\n')
        for i in data[name]:
            f.writelines(str(i)+'\n')"""

    student_data = data[name] # get all records for the student
    # last_entry = None
    # last_exit = None

    # finding most recent entry and exit times for that student
    for record in student_data:
        if record["crossing"] == "ENTER":
            last_entry = record["Time"]
        else:
            last_exit = record["Time"]

    #checking if current time is within range of the last entry and exit times for that student

    if last_entry <= current_time <= last_exit:
        print(f"{name} is currently in the campus")
    else:
        print(f"{name} is not currently in the campus")
    # else:
    #     print(f"{name} has not entered or exited the campus")
        
    with open("studentrecord.txt",'w') as f:
        f.write(str(name)+'\n')
        for i in data[name]:
            f.writelines(str(i)+'\n')



#2. get all students who entered or exited during a specific time

def sort_by_time(item): #to compare times and sort
        _, _, time = item #unpacking tuple elements into three separate variables: _, _, and time.
        hours, minutes, seconds = map(int, time.split(':')) # Split the time string into separate hours, minutes, and seconds
        return 3600 * hours + 60 * minutes + seconds # returns the total number of seconds

def students_bw_time(start_time, end_time):
    entered_students = []
    exited_students = []
    for name, student_data in data.items():
        for entry in student_data:
            student_time = entry["Time"]

            # Check if the student time is within the start and end times
            if start_time <= student_time <= end_time:
                if entry["crossing"] == "ENTER":
                    entered_students.append((name, entry["Gate number"], student_time))
                else:
                    exited_students.append((name, entry["Gate number"], student_time))

    # data = [('Sahil Goyal', '1', '00:17:07'), ('Khushdev Pandit', '3', '00:12:50'), ('Khushdev Pandit', '1', '00:13:12'), ('Khushdev Pandit', '5', '00:14:28'), ('Khushdev Pandit', '1', '00:15:28'), ('Khushdev Pandit', '3', '00:15:38'), ('Khushdev Pandit', '1', '00:16:23'), ('Khushdev Pandit', '1', '00:17:33')]
    
    entered_students_Sorted = sorted(entered_students, key=sort_by_time)
    exited_students_Sorted=sorted(entered_students, key=sort_by_time)

    print(f"Students who entered during this time period: {entered_students_Sorted}")
    print(f"Students who exited during this time period: {exited_students_Sorted}")

    with open("students_within_time_range.txt", "w") as f:
        f.write(f"Students who entered between {start_time} and {end_time}:\n")
        for entry in entered_students:
            f.write(f"{entry[0]}, {entry[1]}, {entry[2]}\n")
        f.write("\n")
        f.write(f"Students who exited between {start_time} and {end_time}:\n")
        for entry in exited_students:
            f.write(f"{entry[0]}, {entry[1]}, {entry[2]}\n")


#3 get all students who entered or exited thru a specific gate
print()

def students_by_gate(gate_no):
    # counters for enter and exit
    enter_ctr = 0
    exit_ctr = 0
    student_ctr = [] # list to store student records
    for name, student_data in data.items():
        for i in range(len(student_data)):

            # if the gate number matches the provided gate number
            if student_data[i]["Gate number"] == gate_no:

                # increment the enter counter and add the record to the list
                if student_data[i]["crossing"] == "ENTER":
                    enter_ctr += 1
                    student_ctr.append({"name": name, "records": [{"crossing": "ENTER", "Gate number": gate_no, "Time": student_data[i]["Time"]}]})
                
                # increment the exit counter and add the record to the list
                else:
                    exit_ctr += 1
                    student_ctr.append({"name": name, "records": [{"crossing": "EXIT", "Gate number": gate_no, "Time": student_data[i]["Time"]}]})
   
    print(f"Number of times students entered through gate {gate_no}: {enter_ctr}")
    print(f"Number of times students exited through gate {gate_no}: {exit_ctr}")
    print("Student record for gate no.",gate,":\n",student_ctr)

# print()
# gate=input("Enter gate no. = ")
# students_by_gate(gate)

print("CHoose option - ")
print("1. Get the record of student by giving name as input")
print('2. Get the students who entered/exited during start time & end time(inputs)')
print('3. Enter gate no. & see no. of times students hv /entered & exited')
a=input("Enter no.")

if a=='1':
    Name=input("Enter name to check whether presnt in campus or not = ")
    currtime=input("ENter current time")
    check_presence(Name, currtime)# Khushdev Pandit

elif a=='2':
    start_time=(input("Enter starting time = "))
    end_time=(input("Enter ending time = "))

    students_bw_time(start_time,end_time)  #00:00:01 , 00:03:00
    
elif a=='3':
    print()
    gate=input("Enter gate no. = ")
    students_by_gate(gate)



print()




"""EXTRA FUNCTION"""
def studentbygate(gate_no):
    student_ctr = {}
    for name, student_data in data.items():
        for i in range(len(student_data)):
            if student_data[i]["Gate number"] == gate_no:
                if student_data[i]["crossing"] == "ENTER":
                    if name in student_ctr:
                        student_ctr[name]["enter"] += 1
                    else:
                        student_ctr[name] = {"enter": 1, "exit": 0}
                else:
                    if name in student_ctr:
                        student_ctr[name]["exit"] += 1
                    else:
                        student_ctr[name] = {"enter": 0, "exit": 1}
    print("Individual student counter: ", student_ctr)
gate=input("Get indiv student records for gate. enter gate no.")
studentbygate(gate)



# def students_by_gate(gate_no):
#     enter_ctr = 0
#     exit_ctr = 0
#     student_ctr = []
#     # print(data.items())
#     for name, student_data in data.items():
        
#         if student_data[0]["Gate number"] == gate_no:
#             if student_data[0]["crossing"] == "ENTER":
#                 enter_ctr += 1
#                 student_ctr.append((name, enter_ctr))
#             else:
#                 exit_ctr += 1
#                 student_ctr.append((name, exit_ctr))
#     print(f"Number of times students entered through gate {gate_no}: {enter_ctr}")
#     print(f"Number of times students exited through gate {gate_no}: {exit_ctr}")
#     print("Individual counts: ", student_ctr)
