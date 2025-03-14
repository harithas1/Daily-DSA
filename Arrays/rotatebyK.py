# Rotate array by K elements

# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .

# Example 2:
# Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
# Output: 9 10 11 3 7 8
# Explanation: Array is rotated to right by 3 position.


# Leetcode: https://leetcode.com/problems/rotate-array/description/

# Approach: 1 

def rotateByKRight(arr,k):
    n=len(arr)
    temp_arr=arr[n-k:]
    for i in range(n-1,k-1,-1):
        arr[i]=arr[i-k]
    arr[:k]=temp_arr


def rotateByKLeft(arr,k):
    n=len(arr)
    temp_Arr=arr[:k]
    for i in range(n-k):
        arr[i]=arr[i+k]
    arr[n-k:]=temp_Arr


def rotateByK1(arr,k,position):
    return rotateByKRight(arr,k) if position.lower()=="right" else rotateByKLeft(arr,k)
    

# arr =[1,2,3,4,5,6,7]
# k=2
# position="right"

arr = [3,7,8,9,10,11]
k=3
position="left"
rotateByK1(arr,k,position)
print(arr)

# Time complexity: O(N)
# Space complexity: O(K)



# --------------------------------------------------------------



# Approach: 2 (Reversal Algorithm)

def reverse(arr,l,r):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

# [1, 2, 3, 4, 5, 6, 7] = [6, 7, 1, 2, 3, 4, 5], k=2
# [1, 2, 3, 4, 5, 7, 6] --> reverse last k elements
# [5,4, 3, 2, 1, 7, 6] --> reverse first k elements
# [6, 7, 1, 2, 3, 4, 5] --> reverse complete array
def rotateByKRight2(arr,k):
    n=len(arr)
    k=k%n
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-k-1)
    reverse(arr,0,n-1)


# [3, 7, 8, 9, 10, 11, 12] = [9, 10, 11, 12, 3, 7, 8], k=3
# [8, 7, 3, 9, 10, 11, 12] --> reverse first k elements
# [8, 7, 3, 12, 11, 10, 9] --> reverse last k elements
# [9, 10, 11, 12, 3, 7, 8] --> reverse complete array
def rotateByKLeft2(arr,k):
    n=len(arr)
    k=k%n
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
def rotateByK2(arr,k,position):
    return rotateByKRight2(arr,k) if position=="right" else rotateByKLeft2(arr,k)

arr =[3, 7, 8, 9, 10, 11, 12]
k = 3
position="left"

# arr =[1,2,3,4,5,6,7]
# k=2
# position="right"

rotateByK2(arr,k,position)
print(arr)


# Time complexity: O(N)
# Space complexity: O(1)