"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

def nullify_matrix(matrix):
    if not matrix:
        return []
    row = [False] * len(matrix)
    col = [False] * len(matrix[0])

    def nullify_row(matrix, row):
        for i in range(len(matrix[0])):
            matrix[row][i] = 0
    
    def nullify_column(matrix, col):
        for i in range(len(matrix)):
            matrix[i][col] = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    
    for i in range(len(row)):
        if row[i]: nullify_row(matrix, i)
    for i in range(len(col)):
        if col[i]: nullify_column(matrix, i)
    
    return matrix

"""
[
    [1, 0, 3],
    [2, 4, 0],
    [5, 5, 5]
]
"""
req = [
    [1, 0, 3],
    [2, 4, 0],
    [5, 5, 5]
]

print(nullify_matrix(req))