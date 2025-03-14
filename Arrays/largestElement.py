# Find the Largest element in an array

# Approach :1
def largestElement1(arr):
    # sort
    n=len(arr)
    for i in range(n-1):
        swap_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[swap_idx]:
                swap_idx=j
        arr[i],arr[swap_idx]=arr[swap_idx],arr[i]
    return arr[-1]


arr=[1,5,4,6,3,7,2]
print(largestElement1(arr))

# Time complexity : O(N*log(N))
# Space complexity: O(1)

# --------------------------------------------------------------


# Approach :2
def largestElement2(arr):
    max_el=arr[0]
    for i in range(1,len(arr)):
        max_el=max(arr[i],max_el)
    return max_el


arr=[1,5,4,6,3,7,2]
print(largestElement2(arr))


# Time complexity : O(N)
# Space complexity: O(1)



