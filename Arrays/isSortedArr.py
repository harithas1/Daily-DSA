# Check if an Array is Sorted

# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.


# Approach: 1 (Optimal Approach)

def isSorted1(arr):
    if len(arr)<=1:
        return True
    n=len(arr)
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False   
    return True

print(isSorted1([5]))
print(isSorted1([5,4,6,7,8]))
print(isSorted1([1,2,3,4,5]))

# Time complexity: O(N)
# Space complexity: O(1)

# --------------------------------------------------------------


# arr=[1,2,3,4,5]

# Approach: 2
def isSorted2(arr):
    n=len(arr)
    for i in range(n):
        cur_el=arr[i]
        for j in range(i+1,n):
            if cur_el>arr[j]:
                return False
    return True

print(isSorted2([5]))
print(isSorted2([5,4,6,7,8]))
print(isSorted2([1,2,3,4,5]))

# Time complexity: O(N^2)
# Space complexity: O(1)

