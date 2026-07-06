matrix_A = [
    [0, 3, -1, 5],
    [0, 4,  2, 6],
    [1, 2,  5, 11]
]


def gaussian_elimination(matrix):
    column_count = len(matrix[0])
    row_count = len(matrix)

    # For loop to check how many pivot points available before last row 
    for pivot in range(min(row_count, column_count) - 1):

        # Conditional and for loop to swap 0 pivot value with non-zero pivot rows
        if matrix[pivot][pivot] == 0:  
                for swap_row in range(pivot+1, row_count):
                    if matrix[swap_row][pivot] !=0:
                        matrix[swap_row], matrix[pivot] = matrix[pivot], matrix[swap_row]
                        break
        # for loop to get factor from the next row of pivot till last row
        for row in range(pivot+1, row_count):
            factor = matrix[row][pivot] / matrix[pivot][pivot]

            # for loop to perform the elimination on columns
            for col in range(column_count):
                matrix[row][col] = matrix[row][col] - (matrix[pivot][col]*factor)
    return matrix

ref_matrix = gaussian_elimination(matrix_A)

for row in ref_matrix:
    print(row)