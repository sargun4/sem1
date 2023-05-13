def RREF(A: list[list]) ->list[list]:
    pivots = []
    pivot = 0
    row = 0
    while row<len(A) and pivot<len(A[0]):
        swap = 0
        while A[row][pivot] == 0:
            if row+swap < len(A):
                temp = A[row]
                A[row] = A[row+swap]
                A[row+swap] = temp         
                swap += 1
            else:
                break
        if row+swap == len(A):
            pivot += 1
            continue
        else:
            A[row] = [i/A[row][pivot] for i in A[row]]
            for i in range(len(A)):
                if i == row:
                    continue
                else:
                    ratio = A[i][pivot]
                    for j in range(len(A[i])):
                        A[i][j] -= ratio*A[row][j]
            pivots.append((row, pivot))
            pivot += 1
            row += 1

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = round(A[i][j],3)

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 0:
                A[i][j] = 0
            elif A[i][j] == 1:
                A[i][j] = 1
    return A, pivots


def parametric(RREF: list[list]) -> list[tuple]:
    para = [("1*", [None for _ in range(len(RREF[0])-1)])]
    pivots = []
    for i in range(len(RREF)):
        for j in range(len(RREF[i])):
            if RREF[i][j] == 1:
                if j == len(RREF[i])-1:
                    print("unconsistant marix")
                    return (0,)
                else:
                    para[0][1][j] = RREF[i][-1]
                    pivots.append(j)
                    break

    free = [i for i in range(len(RREF[0])-1) if i not in pivots]
    
    for i in free:
        para[0][1][i] = 0

    # print(pivots,free)
    for i in free:
        temp = []
        row = 0
        for var in range(len(RREF[0])-1):
            if var == i:
                temp.append(1)
            elif var in free:
                temp.append(0)
            else:
                temp.append(-1*RREF[row][i])
                row += 1
        para.append(("x"+str(i)+"*",temp))
    return para
matrix = [[0,3,-6,6,4,-5], 
        [3,-7,8,-5,8,9], 
        [3,-9,12,-9,6,15]]
print("RREF = ")
M = RREF(matrix)
for i in M[0]:
    print(i)
print("\nPIVOTS")
print(M[1])

print("\n")
for i in parametric(matrix):
    print(i)


    
