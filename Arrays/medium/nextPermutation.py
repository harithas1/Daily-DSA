# next_permutation : find next lexicographically greater permutation

# Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

# Input format:
#  Arr[] = {1,3,2}
# Output
# : Arr[] = {2,1,3}


# Leetcode: https://leetcode.com/problems/next-permutation/description/

# Approach:1 (Bruteforce Approach)

from itertools import permutations
def next_permutation1(arr):
    allPermutations=sorted(set(permutations(arr)))
    for i in range(len(allPermutations)):
        if list(allPermutations[i])==arr:
            return list(allPermutations[i+1]) if i+1<len(allPermutations) else list(allPermutations[0])

print(next_permutation1([1,2,3]))

# TIme Complexity: (N! log N!)
# space complexity: O(N!)



# -------------------------------------------------------------



# Approach:2 (optimal Approach)

def next_permutation2(arr):
    breakpoint=-1
    for i in range(len(arr)-2,-1,-1):
        if arr[i]<arr[i+1]:
            breakpoint=i
            break
    if breakpoint==-1:
        return arr[::-1]
    # find the just greater element of arr[breakpoint] and swap
    for i in range(len(arr)-1,breakpoint,-1):
        if arr[i]>arr[breakpoint]:
            arr[i],arr[breakpoint]=arr[breakpoint],arr[i]
            break
    l,r=breakpoint+1,len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

arr = [2, 1, 5, 4, 3, 0, 0]
next_permutation2(arr)
print(arr)

# Time Complexity: O(3N)
# Space Complexity: O(1) 
