def checkMatrix(A):
	"""Checks if the entries in the input matrix A are integers or not. (for the precondition of MatrixRank() function)"""
	m=len(A)
	n=len(A[0])
	for i in range(m):
		for j in range(n):
			assert isinstance(A[i][j],int),"All the inputs should be of integer type."
def swapRows(A,row1,row2):
	"""Swaps rows row1 with row2 in matrix A.
	Preconditions: row1 and row2 are whole numbers and A is a matrix in the form of nested list."""
	for i in range(len(A[0])):
		A[row1][i],A[row2][i]=A[row2][i],A[row1][i]
def swapColumns(A,col1,col2):
	"""Swaps columns col1 with col2 in matrix A.
	Preconditions: col1 and col2 are whole numbers and A is a matrix in the form of nested list."""
	for i in range(len(A)):
		A[i][col1],A[i][col2]=A[i][col2],A[i][col1]
def Row_Transformation(A,x,row1,row2):
	"""Performs row transformation: row2->row2+x*row1, in matrix A.
	Preconditions: row1 and row2 are whole numbers and A is a matrix in the form of nested list. x can be any real number."""
	for i in range(len(A[0])):
		A[row2][i]=A[row2][i]+x*A[row1][i]
def transpose(A):
	"""Returns the transpose of matrix A.
	Preconditions: A is a matrix in the form of nested list."""
	m=len(A)
	n=len(A[0])
	B=[]
	for i in range(n):
		B.append([])
	for i in range(n):
		for j in range(m):
			B[i].append(A[j][i])
	return B

def MatrixRank(A):
	"""Returns the rank of the matrix A.
	Preconditions: A is a matrix containing integers in the form of nested list."""
	checkMatrix(A)
	m=len(A)
	n=len(A[0])
	rank=n
	row=0
	if m<n:
		A=transpose(A)
		m=len(A)
		n=len(A[0])
		rank=n
	rows=m
	while row<rank:
		if A[row][row]!=0:
			for i in range(m):
				if i!=row:
					x=A[i][row]/A[row][row]
					Row_Transformation(A,-1*x,row,i)
		else:
			cond=True		
			for i in range(row+1,m):
				if A[i][row]!=0:
					cond=False
					break
			if cond==False:
				swapRows(A,i,row)
			elif cond==True:
				swapColumns(A,row,n-1)
				rank=rank-1
				n=n-1
			row=row-1
		row=row+1
	return rank

if __name__ == '__main__':
	pass
