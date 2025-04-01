

# Count Subarray sum Equals K
# Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input Format:
#  N = 4, array[] = {3, 1, 2, 4}, k = 6
# Result:
#  2



# Leetcode: https://leetcode.com/problems/subarray-sum-equals-k/


# Approach: 1 (Better Approach)

def countSubarray(arr,k):
    count=0
    for i in range(len(arr)):
        subarr_sum=0
        for j in range(i,len(arr)):
            subarr_sum+=arr[j]
            if subarr_sum==k:
                count+=1
    return count
print(countSubarray([3, 3, 2, 4],6))

# Time Complexity: O(N^2)
# Space Complexity: O(1)


# --------------------------------------------------------------

# Approach: 2 (Optimal Approach)

def countSubarray2(arr,k):
    prefix_count={0:1}
    prefix_sum=0
    count=0
    for num in arr:
        prefix_sum+=num
        if prefix_sum-k in prefix_count:
            count+=prefix_count[prefix_sum-k]
        prefix_count[prefix_sum]=prefix_count.get(prefix_sum,0)+1
    return prefix_count,count

print(countSubarray2([3, 2, 1, 1, 4, 6],6))

# Time Complexity: O(N)
# Space Complexity: O(N)
