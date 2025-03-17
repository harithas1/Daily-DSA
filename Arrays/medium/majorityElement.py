# Find the Majority Element that occurs more than N/2 times


# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.

# Input Format
#  nums[] = {3,2,3}
# Result  : 3



# Leetcode: https://leetcode.com/problems/majority-element/description/

# Approach: 1 

def majorityElement1(arr):
    n=len(arr)
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    for num,count in freq.items():
        if count>n//2:
            return num
        
print(majorityElement1([3,2,3]))



# Time Complexity: O(N)
# Space COmplexity: O(N)

# --------------------------------------------------------------

# Approach: 2 (Optimal Approach) - Boyer-Moore's Voting Algorithm

def majorityElement2(arr):
    el=arr[0]
    count=1
    for i in range(1,len(arr)):
        if arr[i]==el:
            count+=1
        else:
            if count==1:
                el=arr[i]
            else:
                count-=1
    return el

print(majorityElement2([4,4,2,4,3,4,4,3,2,4]))

# Time Complexity: O(N)
# Space COmplexity: O(1)




