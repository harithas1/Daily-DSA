
#  Kadane's Algorithm : Maximum Subarray Sum in an Array


# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which has the largest sum and returns its sum and prints the subarray.



# Leetcode: https://leetcode.com/problems/maximum-subarray/description/


# Approach: 1

def maxSubArraySum(arr):
    max_sum=0
    n=len(arr)
    
    for i in range(n):
        cur_sum=0
        for j in range(i,n):
            cur_sum+=arr[j]
            max_sum=max(max_sum,cur_sum)
    return max_sum
            
            

print(maxSubArraySum([-2,1,-3,4,-1,2,1,-5,4]))

# Time Complexity: O(N^2)
# Space Complexity: O(1) 

# -------------------------------------------------------------


# Approach: 2 (Optimal Approach)

def maxSubArraySum2(arr):
    max_sum=float("-inf")
    cur_sum=0
    for i in range(len(arr)):
        cur_sum+=arr[i]
        print(max_sum)
        max_sum=max(cur_sum,max_sum)
        if cur_sum<0:
            cur_sum=0
    return max_sum

print(maxSubArraySum2([-2,-1]))

# print(maxSubArraySum2([-2,1,-3,4,-1,2,1,-5,4]))
# Time Complexity: O(N)
# Space Complexity: O(1) 
