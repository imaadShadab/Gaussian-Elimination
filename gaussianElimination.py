matrix_A = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
def gaussian_elimination(matrix):
    column_count = len(matrix[0])
    row_count = len(matrix)

    pivot = 0

    for pivot in range(min(row_count, column_count) - 1):
        for j in range(pivot+1, row_count):
            factor = matrix[j][pivot] / matrix[pivot][pivot]
            for i in range(column_count):
                matrix[j][i] = matrix[j][i] - (matrix[pivot][i]*factor)
                
    for x in matrix:
        print(x)

gaussian_elimination(matrix_A)