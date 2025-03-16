
# Count Maximum Consecutive One's in the array
# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

# Leetcode: https://leetcode.com/problems/max-consecutive-ones/

# Approach:1 (Optimal Approach)


def consecutiveOnes1(arr):
    maxOnes=0
    curOnes=0
    for i in arr:
        if i==1:
            curOnes+=1
            maxOnes=max(curOnes,maxOnes)
        else:
            curOnes=0
    return maxOnes

print(consecutiveOnes1([1, 1, 0, 1, 1, 1]))


# Time complexity : O(N)
# Space complexity: O(1)


# -------------------------------------------------------------


# Approach:2 (Brute Force Approach)

def consecutiveOnes2(arr):
    maxOnes=0
    n=len(arr)
    for i in range(n):
        curOnes=0
        for j in range(i,n):
            if arr[j]==1:
                curOnes+=1
                maxOnes=max(curOnes,maxOnes)
            else:
                break
    return maxOnes


print(consecutiveOnes2([1, 1, 0, 1, 1, 1]))



# Time complexity : O(N^2)
# Space complexity: O(1)
      
        

    