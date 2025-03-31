
# Spiral Traversal of Matrix
# Problem Statement: Given a Matrix, print the given matrix in spiral order.

# Example 1:
# Input: Matrix[][] = { { 1, 2, 3, 4 },
# 		      { 5, 6, 7, 8 },
# 		      { 9, 10, 11, 12 },
# 	              { 13, 14, 15, 16 } }

# Output: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10

# Leetcode: https://leetcode.com/problems/spiral-matrix/description/


def spiralTraversal(arr):
    if not arr:
        return []
    rows=len(arr)
    cols=len(arr[0])
    top, bottom, left, right = 0, rows-1, 0, cols-1 
    result = []
    while top<=bottom and left<=right:
        for col in range(left,right+1):
            result.append(arr[top][col])
        top+=1
        for row in range(top,bottom+1):
            result.append(arr[row][right])
        right-=1

        if top<=bottom:
            for col in range(right,left-1,-1):
                result.append(arr[bottom][col])
            bottom-=1
        if left<=right:
            for row in range(bottom,top-1,-1):
                result.append(arr[row][left])
            left+=1
    return result
            



print(spiralTraversal( [[1, 2, 3, 4] ,
		      [5, 6, 7, 8],
		       [9, 10, 11, 12],
	               [13, 14, 15, 16]]))

# Time Complexity: O(N*M) 
# Space Complexity: O(1)


# We use four boundaries to control the movement:
# top → starting row
# bottom → last row
# left → first column
# right → last column
 # At each step, we move in one direction and then adjust the corresponding boundary.

# 1   2   3   4
# 5   6   7   8
# 9  10  11  12
# 13 14  15  16


# 1st Step: Move Left to Right (Top Row)
# Start from (top, left) → (top, right):
# ➡ 1 → 2 → 3 → 4
# After this, move the top boundary down (top = 1).

# 2nd Step: Move Top to Bottom (Right Column)
# Move from (top, right) → (bottom, right):
# ⬇ 8 → 12 → 16
# After this, move the right boundary left (right = 2).

# 3rd Step: Move Right to Left (Bottom Row)
# Move from (bottom, right) → (bottom, left):
# ⬅ 15 → 14 → 13
# After this, move the bottom boundary up (bottom = 2).

# 4th Step: Move Bottom to Top (Left Column)
# Move from (bottom, left) → (top, left):
# ⬆ 9 → 5
# After this, move the left boundary right (left = 1).

