# Gaussian Elimination

A simple Python implementation of the Gaussian Elimination algorithm written from scratch using plain Python lists. The project demonstrates how a system of linear equations can be solved by first transforming an augmented matrix into **Row Echelon Form (REF)** and then applying **back-substitution**.

The goal of this project is educational: every step of the algorithm is implemented manually without relying on external numerical libraries.

## Features

* Forward elimination using elementary row operations
* Basic partial pivoting (swaps rows when the pivot element is zero)
* Supports rectangular matrices during forward elimination
* Produces the matrix in Row Echelon Form (REF)
* Back-substitution for solving systems of linear equations
* Implemented entirely with native Python lists
* No external dependencies

## Project Structure

```python
gaussian_elimination(matrix)
```

Performs forward elimination and converts an augmented matrix into Row Echelon Form.

```python
back_substitution(U_matrix)
```

Solves the resulting upper triangular system using back-substitution.

## Example

### Input

```python
matrix = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]
```

### Row Echelon Form

```text
[2, 1, -1, 8]
[0.0, 0.5, 0.5, 1.0]
[0.0, 0.0, -1.0, 1.0]
```

### Solution

```python
[2.0, 3.0, -1.0]
```

## Current Limitations

This implementation is intended as a learning project rather than a production-ready numerical solver.

Current limitations include:

* Only performs basic partial pivoting (swaps with the first suitable row below)
* Does not yet detect singular or inconsistent systems
* Does not handle pivot-free columns where an entire pivot column contains zeros
* Modifies the input matrix in place

## Future Improvements

* Full partial pivoting using the largest absolute pivot
* Support for matrices with missing pivot columns
* Reduced Row Echelon Form (RREF)
* Better handling of singular and inconsistent systems
* Input validation
* Deep-copy support to preserve the original matrix
* Automated test suite

## Purpose

This project was built as a learning exercise to understand the mechanics of Gaussian Elimination rather than treating it as a black-box algorithm. The focus is on clarity and readability so that each step of the elimination and back-substitution process can be followed directly from the source code.
