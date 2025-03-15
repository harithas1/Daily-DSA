# Find the missing number in an array


# Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.


# Leetcode: https://leetcode.com/problems/missing-number/

# Approach: 1 (Brute force)
def findMissing1(n,arr):
    for i in range(1,n+1):
        if i not in arr:
            return i 
    return -1
    

arr = [1,2,4,5]
print(findMissing1(5,arr))

# Time complexity: O(n^2)
# Space complexity: O(1)

# --------------------------------------------------------------


# Approach: 2(Better Approach)

def findMissing2(n,arr):
    hash=[0]*(n+1)
    for i in range(len(arr)):
        hash[arr[i]]+=1
    for i in range(1,n):
        if hash[i]==0:
            return i


arr = [1,2,4,5]
print(findMissing2(5,arr))

# Time complexity: O(2*N)
# Space complexity: O(N)



# --------------------------------------------------------------


#  Approach: 3(Optimal Approach)

def findMissing3(n,arr):
    actual_sum=(n*(n+1))//2
    return actual_sum-sum(arr)

arr = [1,2,4,5]
print(findMissing3(5,arr))


# Time complexity: O(N)
# Space complexity: O(1)
