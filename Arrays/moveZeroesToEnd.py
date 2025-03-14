# Move all Zeros to the end of the array


# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.



# 🔗 Leetcode: https://leetcode.com/problems/move-zeroes/description/



# Approach: 1  (Two pointers- Optimal Solution)

arr=[ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
def moveZeroesEnd1(arr):
    n=len(arr)
    i=0
    for j in range(n):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
moveZeroesEnd1(arr)
print(arr)

# Time complexity: O(N) 
# Space complexity: O(1)

# --------------------------------------------------------------



# Approach: 2 (Brute Force)

def moveZeroesEnd2(arr):
    temp_arr=[]
    for i in arr:
        if i!=0:
            temp_arr.append(i)
    for i in range(len(arr)):
        if i<len(temp_arr):
            arr[i]=temp_arr[i]
        else:
            arr[i]=0
    
arr=[ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
moveZeroesEnd2(arr)
print(arr)

# Time complexity: O(N) 
# Space complexity: O(N)

