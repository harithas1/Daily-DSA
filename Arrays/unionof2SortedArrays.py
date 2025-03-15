# Union of Two Sorted Arrays
# Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

# The union of two arrays can be defined as the common and distinct elements in the two arrays.NOTE: Elements in the union should be in ascending order.

def union1(arr1,arr2):
    temp_arr=set()
    for i in arr1:
        temp_arr.add(i)
    for j in arr2:
        temp_arr.add(j)

    return sorted(temp_arr)



arr1 = [1,2,4,5]
arr2 = [3,4,4,5]

print(union1(arr1,arr2))
    
    
# Time complexity: O(M+N+ U log U) (U = unique elements)
# Space complexity: O(U)

# --------------------------------------------------------------

def union2(arr1,arr2):
    i=0
    j=0
    temp=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            if len(temp) ==0 or temp[-1]!=arr1[i]:
                temp.append(arr1[i])
            i+=1
        else:
            if len(temp)==0 or temp[-1]!=arr2[j]:
                temp.append(arr2[j])
            j+=1
    while i<len(arr1):
        if temp[-1]!=arr1[i]:
            temp.append(arr1[i])
        i+=1

    while j<len(arr2):
        if temp[-1]!=arr2[j]:
            temp.append(arr2[j])
        j+=1
    return temp

arr1 = [1,2,4,5]
arr2 = [3,4,4,5]


print(union2(arr1,arr2))

# Time complexity: O(M+N)
# Space complexity: O(M+N)