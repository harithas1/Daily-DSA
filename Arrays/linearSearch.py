# Linear Search

# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

def linearSearch(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1
    
print(linearSearch([1,2,3,4,5],3))



# Time complexity: O(N) 
# Space complexity: O(1)