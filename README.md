# Gaussian-Elimination
A simple Python implementation of the Gaussian Elimination algorithm that transforms a matrix into row echelon form (REF).

## Features
- Forward elimination using elementary row operations
- Supports rectangular matrices
- Produces the matrix in row echelon form
- Lightweight implementation using plain Python lists (no external libraries)

## Planned Features
- Partial pivoting for improved numerical stability
- Back substitution to solve systems of linear equations
- Reduced Row Echelon Form (RREF) option
- Input validation and handling for singular matrices

### Example
matrix = [ [1, 2, 3], [3, 4, 5], [5, 6, 7], [3, 6, 9] ]

gaussian_elimination(matrix)

Output:

[1, 2, 3] [0.0, -2.0, -4.0] [0.0, 0.0, 0.0] [0.0, 0.0, 0.0]

This project is intended as an educational implementation to demonstrate the mechanics of Gaussian elimination before adding more advanced features such as pivoting and complete linear system solving.
