
# Sort an array of 0s, 1s and 2s

# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

# Input: nums = [2,0,2,1,0,1,0]
# Output: [0,0,0,1,1,2,2]


# Leetcode: https://leetcode.com/problems/sort-colors/description/

# Approach: 1 (over writing)

def sort1(arr):
    c0=0
    c1=0
    c2=0
    for i in arr:
        if i==0:
            c0+=1
        elif i==1:
            c1+=1
        else:
            c2+=1
    for i in range(c0):
        arr[i]=0
    for i in range(c0,c1+c0):
        arr[i]=1
    for i in range(c0+c1,len(arr)):
        arr[i]=2
    



arr=[2,0,2,1,0,1,0]
sort1(arr)
print(arr)


# Time Complexity: O(N)
# Space COmplexity: O(1)




# --------------------------------------------------------------

# Approach: 2 (Optimal Approach)

def sort2(arr):
    l=0
    mid=0
    r=len(arr)-1
    while mid<=r:
        if arr[mid]==0:
            arr[l],arr[mid]=arr[mid],arr[l]
            l+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[r]=arr[r],arr[mid]
            r-=1
   

        
arr=[2,0,2,1,0,1,0]
sort2(arr)
print(arr)

# Time Complexity: O(N)
# Space COmplexity: O(1)
