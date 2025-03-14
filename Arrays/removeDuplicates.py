# Remove Duplicates in-place from Sorted Array

# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

# If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

# Example 1:
# Input:
#  arr=[1,1,2,2,2,3,3]

# Output:
#  arr[1,2,3,_,_,_,_]


# Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


# Approach: 1 (Optimal Approach)

def removeDuplicates1(arr):
        n=len(arr)
        i=0
        for j in range(1,n):
            if arr[i]!=arr[j]:
                i+=1
                arr[i]=arr[j]
        return i+1
    

arr = [1,1,2,2,2,3,3]
print(arr[:removeDuplicates1(arr)])

# Time complexity: O(N)
# Space complexity: O(1)



# --------------------------------------------------------------



# Approach: 2 (Brute force)

def removeDuplicates2(arr):
    unique_set=set()
    for i in arr:
        unique_set.add(i)
    n=len(unique_set)
    j=0
    for i in unique_set:
        arr[j]=i
        j+=1
    return arr[:n]


arr = [1,1,2,2,2,3,3]
print(removeDuplicates2(arr))


# Time complexity: O(N) 
# Space complexity: O(N)