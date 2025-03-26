# Set Matrix Zero

# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

# Examples 1:

# Input:
#  matrix=[[1,1,1],[1,0,1],[1,1,1]]

# Output:
#  [[1,0,1],[0,0,0],[1,0,1]]

# Leetcode: https://leetcode.com/problems/set-matrix-zeroes/description/


# Approach :1 (Brute force Approach)

def markrow(arr,rows,cols,row):
    for col in range(cols):
        if arr[row][col]!=0:
            arr[row][col]=-1

def markcol(arr,rows,cols,col):
    for row in range(rows):
        if arr[row][col]!=0:
            arr[row][col]=-1

def setMatrixZero(arr):
    rows=len(arr)
    cols=len(arr[0])
    for row in range(rows):
        for col in range(cols):
            if arr[row][col]==0:
                markrow(arr,rows,cols,row)
                markcol(arr,rows,cols,col)
    for row in range(rows):
        for col in range(cols):
            if arr[row][col]==-1:
                arr[row][col]=0
        
                
    # return idx
arr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setMatrixZero(arr)
print(arr)

# Time Complexity: O((N*M)*(N + M)) + O(N*M)
# Space Complexity: O(1) 

# --------------------------------------------------------------


# Approach :2 (Better Approach)

def setMatrixZero1(matrix):
    n=len(matrix)
    m=len(matrix[0])
    rows=[0]*n
    cols=[0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                rows[i]=1
                cols[j]=1
    for i in range(n):
        for j in range(m):
            if rows[i] or cols[j]:
                matrix[i][j]=0
    # return matrix
arr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setMatrixZero1(arr)
print(arr)


# Time Complexity: O(2*(N*M))
# Space Complexity: O(N) + O(M)

# --------------------------------------------------------------

# Approach: 3 (Optimal Approach)


def setMatrixZero2(matrix):
    n=len(matrix)
    m=len(matrix[0])

    col0=1
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                matrix[i][0]=0 # mark i-th row:
                if j!=0:
                    matrix[0][j]=0
                else:
                    col0=0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]!=0:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
    if matrix[0][0]==0:
        for j in range(m):
            matrix[0][j]=0
    if col0==0:
        for i in range(n):
            matrix[i][0]=0
    return matrix

arr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setMatrixZero2(arr)
print(arr)