# matrix = [[0,3,-6,6,4,-5], [3,-7,8,-5,8,9],[3,-9,12,-9,6,15]]
print()
# matrix=[[1,-3, 3, -2],[-3 ,7 ,-1 ,2],[0 ,1, -4 ,3]]
# matrix=[[1,-1,-1,3],[1,1,-2,1],[4,-2,4,1]]
# matrix=[[3,5,-4],[-3,-2,4],[6,1,-8]]
# 3
# 5
# 1 -2 -1 3 0
# -2 4 5 -5 3
# 3 -6 -6 8 2 

# matrix=[[1,0,0],[0,2,0],[0,0,1],[0,1,3]]
# matrix=[[1,6,2,-5,-2,-4],[0,0,2,-8,-1,3],[0,0,0,0,1,7]]
# matrix=[[0,0,2,0,4],[0,8,0,0,1],[8,0,9,0,3],[8,0,0,5,1]]
# matrix=[[0,0,3],[0,5,6],[0,8,9]]

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# matrix=[[0,0,3,5,6,8,-9,11,4],[0,0,6,2,1,0,3,2,1],[1,8,-9,1,5,7,0,-6,-1],[0,0,-9,1,5,7,0,14,-1],[5,0,-9,1,5,7,0,3,0]]
# matrix=[[1,2,-1,-4],[2,3,-1,-11],[-2,0,-3,22]]


#1st method-
# rows=int(input("Enter no of rows = "))
# cols=int(input("Enter no of cols = "))
# matrix=[[int(i) for i in input().split()[:cols]] for i in range(rows)]


#2nd method-read frm file
#to read matrix from mathasgn.txt text file
with open('mathasgn.txt','r') as f:
    r=f.readlines()
    # print(r)
    rows=int(r[0][:-1])
    cols=int(r[1][:-1])
    # for i in r:
        #     print(i[:-1])
    print(rows)
    print(cols)
    matrix=[]
    for i in range(2, len(r)):
    # Split the current line into a list of integers
        row = [int(x) for x in r[i].strip().split()]
        # Append the row to the matrix
        matrix.append(row)

    # Print the matrix to verify that it was created correctly
    for row in matrix:
        print(row)



def rref(A):
    #first REF is calc.
    n = len(A) #no of rows
    m = len(A[0]) #no of cols
    for i in range(n):
        if i >= m:
            break
        for j in range(i, n): 
            if j >= n:
                break             
            zero_elmnt = A[j][i]  # finding the first row with a nonzero element in first column
            if zero_elmnt == 0:
                continue #If curr element is zero, the inner loop continues with the next iteration.
            A[i],A[j]=A[j],A[i] #swapping rows
            diag_elmnt = A[i][i]
            # if diag_elmnt == 0:
            #         A[i],A[j]=A[j],[i]
            #         diag_elmnt=A[i][i]
            for row in range(i + 1, n):     # iterates through the rows below the current row
                # subtracting multiples of the new first row to lower rows inorder to make lower entries of first column zero
                factor = -(A[row][i] / diag_elmnt) #for row operation
                for col in range(i, m):# columns of the current row i
                    A[row][col] += (factor*A[i][col] )#crrent element is updated by adding the product of the ith row and factor
            break
    # print("REF = ", A)

    #For RREF
    for i in range(min(n, m) - 1, -1, -1):
        # dividing last non-zero row by first non-zero element
        first_elem = -1
        
        first_elem_col = -1
        for c in range(m):
            if A[i][c] == 0:
                continue #If the current element is zero, inner loop continues with next iteration

            if first_elem_col == -1:
                first_elem = A[i][c]
                first_elem_col = c
                
            A[i][c] /= first_elem
        # adding multiples of this row to make numbers above the leading 1=zero
        for j in range(i):
            elmnt_above_rowj = A[j][first_elem_col]# value of element in the row above the current row j,
                    # located at the column of the first non-zero element (first_elem_col) in the current row i.
            factor = -(elmnt_above_rowj)
            for col in range(m):
                A[j][col] +=  factor*A[i][col]
        
    return (A)

rref_matrix = rref(matrix)

#for rounding off values in rref mat
for i in range(len(rref_matrix)):
    for j in range(len(rref_matrix[0])):
        rref_matrix[i][j]=round((rref_matrix[i][j]),3)
        
print("RREF matrix(UNAUGMENTED):")
for row in rref_matrix:
    print(row)


basic_vars = []
free_vars=[]
xlist=["x" + str(i + 1) for i in range(len(rref_matrix[0]))] #list of variable names(x1,x2,x3...)
# print(xlist)
for i, row in enumerate(rref_matrix):
    leading_col = -1 #initialize variable to store the leading column
    for j, val in enumerate(row):
        if val == 1:
            leading_col = j   # If the value is 1, set the leading column to the current column
            break
    if leading_col != -1:# If there is a leading column (i.e. a row with a leading 1)
        basic_vars.append("x" + str(leading_col + 1))
        # if "x" + str(leading_col + 1) in free_vars:
        #     free_vars.remove("x" + str(leading_col + 1))
    
for i in xlist:
    if i not in basic_vars:
        free_vars.append(i)

# print("\nbasic variables:", basic_vars)
# print("free variables:", free_vars)



#FIRST AUGMENT WITH 0 COL MATRIX AND THEN FORM PARAM EQNS;

def augment_matrices(mat1, mat2):
    # mat2's columns added to the right of mat1(AUGMENT) and return augmented mat.
    augmntd_mat = []
    for i in range(len(mat1)):
        j = mat1[i]
        newrow = j[:] + mat2[i]
        augmntd_mat.append(newrow)
    return augmntd_mat

def vector_to_colmat(vector):
    """Convert a vector into a column matrix."""
    augmntd_col = []
    for j in vector:
        augmntd_col.append([j])
    return augmntd_col

a=[0 for i in range(len(rref_matrix))]
augmntd_col = vector_to_colmat(a) # Augment the rref with a column of zeros
finalrref = augment_matrices(rref_matrix, augmntd_col)
print("\nfinal rref (AUGMENTED)=")
for row in finalrref:
    print(row)


#param form
def parametric_form(finalrref, variables):
    m, n = len(finalrref), len(finalrref[0])
    solution = []

    for i in range(m):  
        row = finalrref[i]
        if i<len(basic_vars):
            basic_var = basic_vars[i]  
            equation = f"{basic_var} = "  #to show ans in req. format
        
        else:
            pass
        # print(equation)

        for j in range(n):
            if row[j] != 0:
                if variables[j] not in basic_vars:

            
                    equation += f"{-row[j]} * {variables[j]} + "
            # print(equation)
        equation += f"{row[-1]}"
        solution.append(equation)
    # print(solution)
    
    return solution, basic_vars, free_vars

xlist=["x" + str(i + 1) for i in range(len(finalrref[0]))]
solution, basic_vars, free_vars = parametric_form(finalrref, xlist)

print("\nSOLUTION in terms of EQUATIONS:")
for eq in solution:
    print(eq)
print("\nBasic variables:", basic_vars)
print("Free variables:", free_vars)


def parametric(rref) : # will accept rref mat & return final paramtric form
    pivots = []
    colvector = [("1*", ["freevar" for x in range(len(rref[0])-1)])] #col vectors corresp to free vars 
    m=len(rref)
    n=len(rref[0])

    for i in range(m):
        for j in range(n):
            if rref[i][j] == 1:
                # if j == n-1:
                #     print("inconsistent")
                #     return (0,)
                # else:
                colvector[0][1][j] = rref[i][-1]
                pivots.append(j)
                break
    # print(colvector) #initially shows constant col. vector eg:if x4 is free and x1,x2,x3,x5 are basic [0,0,0,freevar,0] 
                   #  it dentotes that 4th idx is supposed to be location of x4-which is freevar(random eg)-stored as list of tup
    # print(pivots)
    freevalsub1=[]  # denotes lst which will be containing (free_vars-1) to avoid INdexError
    for i in free_vars:
        freevalsub1.append(int(i[1])-1)#here freevalsub1 contains free_vars (value-1)
    # freevalsub1 = [(i) for i in range(n-1) if i not in pivots] 
    # print(freevalsub1)
    for i in freevalsub1:
        colvector[0][1][i] = 0
        # print(colvector[0][1][i])

    # print(freevalsub1) # contains free_vars' (value-1) ; sub means -
    for i in freevalsub1:
        colvect_temp = [] #temp list which will store col vectors corresp to free vars
        row = 0
        for x in range(n-1):
            if x == i:
                colvect_temp.append(1)   #placing 1 at freevalsub1 vars corresponding colvector at its(index-1)  
            elif x in freevalsub1:
                colvect_temp.append(0)  #else append(0) to other places in colvector 
            else:
                colvect_temp.append(-rref[row][i]) #appending val
                row += 1
        colvector.append(("x"+str(i+1)+"*",colvect_temp)) 
    return colvector #list of tupls with free var at tup[0] & col vect corresp to it at tup[1]

# print(parametric(finalrref))
result = parametric(finalrref)
# print(result)
finalparamform = "x = " + result[0][0] + str(result[0][1])
for i in range(1, len(result)):
    finalparamform += " + " + result[i][0] + str(result[i][1])

print("\nSOLUTION:")
print(finalparamform)


