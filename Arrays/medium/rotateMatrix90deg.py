# Rotate Image by 90 degree

# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

# Note: Rotate matrix 90 degrees anticlockwise

# Input:
#  [[1,2,3],[4,5,6],[7,8,9]]

# Output
# : [[7,4,1],[8,5,2],[9,6,3]]



# Leetcode: https://leetcode.com/problems/rotate-image/submissions/1586651299/


# Approach: 1 (Bruteforce)

def rotateMatrix1(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    result_matrix=[[0]*rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            result_matrix[col][rows-1-row]=matrix[row][col]
    return result_matrix

print(rotateMatrix1([[1,2,3],[4,5,6],[7,8,9]]))

# Time Complexity: O(M × N)
# Space Complexity: O(M × N) 


# --------------------------------------------------------------


# Approach:2 (Optimal)

def rotateMatrix2(matrix):
    n=len(matrix)
    for row in range(n):
        for col in range(row):
            matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]
    for i in range(n):
        matrix[i].reverse()
    
matrix=[[1,2,3],[4,5,6],[7,8,9]]
rotateMatrix2(matrix)
print(matrix)

# Time Complexity: O(N*N) + O(N*N)
# Space Complexity: O(1)