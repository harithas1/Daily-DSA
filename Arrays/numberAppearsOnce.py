# Find the number that appears once, and the other numbers twice

# Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

# Leetcode: https://leetcode.com/problems/single-number/


# Approach:1 (Brute Force Approach)

def numAppearsOnce1(arr):
    freq={}
    for i in range(len(arr)):
        freq[arr[i]]=freq.get(arr[i],0)+1
    for num,count in freq.items():
        if count==1:
            return num,freq
    return -1
        
print(numAppearsOnce1([2,2,1]))


# Time complexity : O(N)
# Space complexity: O(N)


# --------------------------------------------------------------


# Approach:2 (Optimal Approach - XOR)

def numAppearsOnce2(arr):
    unique=0
    for i in arr:
        unique ^=i
    return unique

print(numAppearsOnce2([2,2,1]))


# Time complexity : O(N)
# Space complexity: O(1)

