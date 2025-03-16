
# Longest Subarray with given Sum K(Positives)

# Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.


def longestSumSubArray1(arr,target):
    length=0
    
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s+=arr[j]  
            if s==target:
                length=max(length,j-i+1)
           
    return length

arr = [2, 3, 5, 1, 9]

print(longestSumSubArray1(arr,5))

# Time complexity : O(N^2)
# Space complexity: O(1)

# ------------------------------------------------------------


# Approach: 2 

def longestSumSubArray2(arr,target):
    max_length=0
    cur_sum=0
    sum_idx_map={}
    
    for i in range(len(arr)):
        cur_sum += arr[i]
        if cur_sum == target:
            max_length = i+1
        if cur_sum - target in sum_idx_map:
            max_length = max(max_length, i - sum_idx_map[cur_sum - target])
        if cur_sum not in sum_idx_map:
            sum_idx_map[cur_sum] = i
        
    return max_length


arr = [2, 3, 5, 1, 9]

print(longestSumSubArray2(arr,5))

# Time complexity : O(N)
# Space complexity: O(1)


        
