# Find Second Smallest and Second Largest Element in an array

# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.


# Approach :1 
def secondLargestSmallest1(arr):
    if len(arr)<=1:
        return f"second minimum: -1 \n second largest: -1"
    min_el=arr[0]
    max_el=arr[0]
    for i in range(1,len(arr)):
        min_el=min(min_el,arr[i])
        max_el=max(max_el,arr[i])
    sec_min=max_el
    sec_max=min_el
    # print(min_el,max_el)
    min_el_diff=max_el-min_el
    max_el_diff=max_el-min_el
    for i in range(len(arr)):
        cur_diff=min((arr[i]-min_el),min_el_diff)
        if cur_diff<min_el_diff and arr[i]!=min_el:
            sec_min=arr[i] 
            min_el_diff=cur_diff
        cur_diff=min((max_el-arr[i]),max_el_diff)
        if cur_diff<max_el_diff and arr[i]!=max_el:
            sec_max=arr[i]
            max_el_diff=cur_diff
       
    return f"second minimum: {sec_min} \n second largest: {sec_max}"
        

arr1=  [1,2,4,7,7,5]
arr2=[1]
print(secondLargestSmallest1(arr1))
print(secondLargestSmallest1(arr2))


# Time complexity : O(N)
# Space complexity: O(1)

# --------------------------------------------------------------



# Approach :2 (BEST SOLUTION)

def secondLargestSmallest2(arr):
    if len(arr)<=1:
        return f"second minimum: -1 \n second largest: -1"
    min_el=float("inf")
    sec_min=float("inf")

    max_el=float("-inf")
    sec_max=float("-inf")
    for i in range(len(arr)):
        if arr[i]<min_el:
            min_el=arr[i]
        if arr[i]>max_el:
            max_el=arr[i]
        elif arr[i]<sec_min and arr[i]!=min_el:
            sec_min=arr[i]
        elif arr[i]>sec_max and arr[i]!=max_el:
            sec_max=arr[i]
    return f"second minimum: {sec_min} \n second largest: {sec_max}"

arr3 = [4,1,2,7,7,5]
arr4=[1]
print(secondLargestSmallest2(arr3))
print(secondLargestSmallest2(arr4))

# Time complexity : O(N)
# Space complexity: O(1)

        


