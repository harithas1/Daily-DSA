
# Longest Subarray with sum K | [Postives and Negatives]


# Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

# Approach: 1 

def longestSubArray1(arr,target):
    max_length=0
    for i in range(len(arr)):
        cur_sum=0
        for j in range(i,len(arr)):
            cur_sum+=arr[j]
            if cur_sum==target:
                max_length=max(max_length,j-i+1)
    return max_length

arr = [-1, 1, 1]
print(longestSubArray1(arr,1))

# Time complexity : O(N^2)
# Space complexity: O(1)


# --------------------------------------------------------------

# Approach: 2 (Optimal Approach)

def longestSubArray2(arr,target):
    cur_sum=0
    max_len=0
    sum_idx_map={}
    for i in range(len(arr)):
        cur_sum+=arr[i]
        if cur_sum==target:
            max_len=i+1
        if cur_sum-target in sum_idx_map:
            length=i-sum_idx_map[cur_sum-target]
            max_len=max(max_len,length)
        if cur_sum not in sum_idx_map:
            sum_idx_map[cur_sum]=i
    return max_len

arr = [-1, 1, 1]
print(longestSubArray2(arr,1))

# Time complexity : O(N)
# Space complexity: O(N)
