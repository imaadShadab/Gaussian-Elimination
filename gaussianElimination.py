matrix_A = [
    [0, 2, 1, 4],
    [1, 3, 2, 8],
    [2, 1, 1, 7]
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


def back_substitution(U_matrix):
    row_count = len(U_matrix)
    column_count = len(U_matrix[0])
    solution_list = [0] * row_count


    for row in range(row_count-1,-1,-1):
        rhs = U_matrix[row][-1]
        pivot = U_matrix[row][row]
        known_sum = 0
        for col in range(row + 1, column_count - 1):
            known_sum += U_matrix[row][col] * solution_list[col]

        solution = (rhs - known_sum) / pivot
        solution_list[row] = solution
    
    return solution_list

echelon_matrix = gaussian_elimination(matrix_A)

print("U-Matrix:")
for row in echelon_matrix:
    print(row)
    
solutions = back_substitution(echelon_matrix)

print("")
print("Solutions:")
print(solutions)