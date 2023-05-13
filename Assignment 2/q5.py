sc_mat = [[0 for i in range(3)] for i in range(3)]  # scaling matrix
print("Enter scaling parameters,cx & cy =")
# scaling parameters
cx = int(input("cx = "))
cy = int(input("cy = "))
sc_mat[0][0] = cx
sc_mat[1][1] = cy
sc_mat[2][2] = 1

coordinate_list = list(tuple(map(int, input("Enter coordinates = ").split()))
                       for r in range(int(input('enter no of coordinates : '))))
#SIZE OF LIST= NO OF COORDINATES  
print("Coordinate list = ", coordinate_list)
print()
n = int(input("Enter size of list = "))
print()
l = [[0 for x in range(3)] for i in range(n)]

for i in range(n):
    for j in range(3):
        l[i][0] = (coordinate_list[i][0])

for i in range(n):
    for j in range(3):
        l[i][1] = (coordinate_list[i][1])

for i in range(n):
    for j in range(3):
        if i == 3-1 or j == 3-1:
            l[i][2] = 1
print()
print("COORDINATE MATRIX = ")
for i in l:
    print(*i)
print()
print("SCALING MATRIX = ")
for i in sc_mat:
    print(*i)

result = [[0 for i in range(3)] for i in range(n)]

for i in range(len(l)):
    for j in range(len(sc_mat[0])):
        for k in range(len(sc_mat)):
            result[i][j] += l[i][k] * sc_mat[k][j]
print()
print("RESULT MATRIX = ")
for i in result:
    print(*i)
print()
l1 = []
print("List of final coordinates = ")

l = [result[i][0:2] for i in range(0, n)]
print(l)
