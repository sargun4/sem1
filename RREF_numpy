import numpy as np

def rref_with_parametric_solution(matrix):
    mat = np.array(matrix)
    m, n = mat.shape

    # Perform Gaussian elimination
    lead = 0
    parametric_soln = []
    for r in range(m):
        if lead >= n:
            break
        i = r
        while mat[i, lead] == 0:
            i += 1
            if i == m:
                i = r
                lead += 1
                if lead == n:
                    break
        mat[[i, r]] = mat[[r, i]]
        lv = mat[r, lead]
        mat[r] = mat[r] / lv

        for i in range(m):
            if i != r:
                mat[i] -= mat[i, lead] * mat[r]

        lead += 1

    # Extract the parametric solution
    for r in range(m):
        row = mat[r]
        pivot_index = np.argmax(row)
        if row[pivot_index] == 1 and np.count_nonzero(row[:pivot_index]) == 0 and np.count_nonzero(row[pivot_index+1:]) == 0:
            # The row is a pivot row with a unique solution
            parametric_soln.append(f'x{pivot_index + 1} = {row[-1]}')
        else:
            # The row has a free variable, add it to parametric solution
            equation = ''
            for c in range(n - 1):
                coefficient = row[c]
                if coefficient != 0:
                    variable = f'x{c + 1}'
                    sign = '-' if coefficient < 0 else '+'
                    equation += f' {sign} {abs(coefficient)}{variable}'
            equation += f' = {row[-1]}'
            parametric_soln.append(equation)

    return mat[:, :-1], parametric_soln

matrix = [[1, 2, 3, 9],
          [2, 3, 4, 12],
          [3, 4, 5, 15]]

rref_matrix, solution = rref_with_parametric_solution(matrix)

print("Row Reduced Echelon Form:")
print(rref_matrix)

print("\nParametric Solution:")
for equation in solution:
    print(equation)
