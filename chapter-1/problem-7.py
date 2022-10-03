"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

"""
Because we're rotating the matrix by 90 degrees, the easiest way to do this is to implement the rotation in
layers. We perform a circular rotation on each layer, moving the top edge to the right edge, the right edge
to the bottom edge, the bottom edge to the left edge, and the left edge to the top edge.
How do we perform this four-way edge swap? One option is to copy the top edge to an array, and then
move the left to the top, the bottom to the left, and so on. This requires O(N) memory, which is actually
unnecessary.

A better way to do this is to implement the swap index by index. In this case, we do the following:
1 for i = 0 to n
2 temp= top[i];
3 top[i] = left[i]
4 left[i] = bottom[i]
5 bottom[i] = right[i]
6 right[i] = temp
"""

def rotate_matrix(matrix: list) -> list:
    if len(matrix) == 0 or len(matrix) != len(matrix[0]): return False

    n = len(matrix)
    for layer in range(int(n / 2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last-offset][first]
            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            # right -> bottom
            matrix[last][last-offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
    return matrix

# Time complexity is O(n2)
"""
[[1, 2, 3, 4], 
 [5, 6, 7, 8], 
 [9, 10, 11, 12], 
 [13, 14, 15, 16]
]
"""
req = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
res = rotate_matrix(req)
for l in res:
    print(l)

"""
[13, 9, 5, 1]
[14, 10, 6, 2]
[15, 11, 7, 3]
[16, 12, 8, 4]
"""

