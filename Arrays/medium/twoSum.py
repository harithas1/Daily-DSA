# Two Sum : Check if a pair with given sum exists in Array

# Problem Statement: Given an array of integers arr[] and an integer target.

# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.


# Leetcode: https://leetcode.com/problems/two-sum/description/

def twoSum1(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return "YES",[i,j]
    return "NO",[-1,-1]

print(twoSum1([2,6,5,8,11],14))



# Time Complexity: O(N^2)
# Space COmplexity: O(1)

# --------------------------------------------------------------



# Approach: 2

def twoSum2(arr,target):
    sum_idx_map={arr[0]:0}
    for i in range(1,len(arr)):
        if target- arr[i] in sum_idx_map:
            return "YES", [sum_idx_map[target-arr[i]],i]
        sum_idx_map[arr[i]]=i
    return "NO",[-1,-1]

print(twoSum2([2,6,5,8,11],14))

# Time Complexity: O(N)
# Space COmplexity: O(N)

# --------------------------------------------------------------

# Approach: 3

def twoSum3(arr,target):
    arr.sort()
    l=0
    r=len(arr)-1
   
    while l<r:
        print(l,arr[l])
        if arr[l]+arr[r]==target:
            
            return "YES", [l,r]
        elif arr[l]+arr[r]>target:
            r-=1
        else:
            l+=1
    return "NO",[-1,-1]

print(twoSum3([2,6,5,8,11],14))


# Time Complexity: O(N log N)
# Space COmplexity: O(N)