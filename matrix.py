import numpy as np

# Define functions related to matrices
def create_matrix(rows, cols):
    """Create a matrix of custom size."""
    return np.zeros((rows, cols))

def add_matrices(matrix1, matrix2):
    """Add two matrices."""
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    """Subtract two matrices."""
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    """Multiply two matrices."""
    return np.dot(matrix1, matrix2)

def transpose_matrix(matrix):
    """Transpose a matrix."""
    return np.transpose(matrix)

# Example using the functions
matrix_a = create_matrix(2, 3)
matrix_b = create_matrix(3, 2)

matrix_a[0][0] = 1
matrix_a[0][1] = 2
matrix_a[0][2] = 3
matrix_a[1][0] = 4
matrix_a[1][1] = 5
matrix_a[1][2] = 6

matrix_b[0][0] = 7
matrix_b[0][1] = 8
matrix_b[1][0] = 9
matrix_b[1][1] = 10
matrix_b[2][0] = 11
matrix_b[2][1] = 12

result_add = add_matrices(matrix_a, matrix_b)
result_subtract = subtract_matrices(matrix_a, matrix_b)
result_multiply = multiply_matrices(matrix_a, matrix_b)
result_transpose = transpose_matrix(matrix_a)

print("Matrix addition:")
print(result_add)

print("Matrix subtraction:")
print(result_subtract)

print("Matrix multiplication:")
print(result_multiply)

print("Transpose of a matrix:")
print(result_transpose)

# add 2 matrix
def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrix dimensions are not suitable for addition."

    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

# Example of using the function
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]

result = add_matrices(matrix1, matrix2)

if isinstance(result, str):
    print(result)
else:
    for row in result:
        print(row)
