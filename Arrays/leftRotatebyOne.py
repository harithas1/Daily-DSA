# Left Rotate the Array by One
# Problem Statement: Given an array of N integers, left rotate the array by one place.

# Input:
#  N = 5, array[] = {1,2,3,4,5}
# Output:
#  2,3,4,5,1


def rotate1(arr):
    n=len(arr)
    if n<=2:
        return arr[::-1]
    last_el=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    
    arr[n-1]=last_el


arr=[1,2,3,4,5]
rotate1(arr)
print(arr)


# Time complexity: O(N)
# Space complexity: O(1)



# --------------------------------------------------------------


def rotate2(arr):
    n=len(arr)
    temp_arr=[0]*n
    for i in range(1,n):
        temp_arr[i-1]=arr[i]
    temp_arr[n-1]=arr[0]
    arr[::]=temp_arr
    # or return temp_arr


arr=[1,2,3,4,5]
rotate2(arr)
print(arr)


# Time complexity: O(N)
# Space complexity: O(N)
