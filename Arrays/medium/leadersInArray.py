# Leaders in an Array

# Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.

# Example 1:
# Input:
# arr = [4, 7, 1, 0]
# Output: [7, 1, 0]


# Example 2:
# Input:
# arr = [10, 22, 12, 3, 0, 6]
# Output: [22, 12, 6]

# gfg Practice: https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

# -------------------------------------------------------------




# Approach: 1(Bruteforce Approach)

def leaders1(arr):
    leaders=[]
    for i in range(len(arr)):
        leader=True
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                leader=False
                break
        if leader:
            leaders.append(arr[i])
    return leaders


print(leaders1([10, 22, 12, 3, 0, 6]) )



# -------------------------------------------------------------

# Approach: 2(Optimal Approach)

def leaders2(arr):
    cur_el=arr[-1]
    print(cur_el,end=", ")
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>cur_el:
            print(arr[i],end=", ")
            cur_el=arr[i]

leaders2([10, 22, 12, 3, 0, 6])  # 6, 12, 22,

# time complexity: O(N)
# Space complexity: O(1)



def leaders3(arr):
    leadersArr=[arr[-1]]
    cur_el=arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>cur_el:
            leadersArr.append(arr[i])
            cur_el=arr[i]
    return leadersArr[::-1]


print(leaders3([10, 22, 12, 3, 0, 6])) # [22, 12, 6]

# time complexity: O(2N)
# Space complexity: O(N)