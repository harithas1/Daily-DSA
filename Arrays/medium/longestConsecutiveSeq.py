# Longest Consecutive Sequence in an Array


# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.

# Approach :1 (Better Approach)

def longestConsecutiveSeq1(arr):
    n=len(arr)
    if n==0:
        return 0
    
    arr.sort()
    last_smaller=float('-inf')
    cnt=0
    longest=1

    for i in range(n):
        if arr[i]-1==last_smaller:
            cnt+=1
            last_smaller=arr[i]
        elif arr[i]!=last_smaller:
            last_smaller=arr[i]
            cnt=1
        longest=max(longest,cnt)
    return longest

arr = [100, 200, 1, 2, 3, 4]

print(longestConsecutiveSeq1(arr))

# Time Complexity: O(NlogN) + O(N)
# Space Complexity: O(1)


# --------------------------------------------------------------

# Appproach :2 (Optimal Approach)

def longestConsecutiveSeq2(arr):
    num_set=set(arr)
    longest_length=0
    for num in num_set:
        if num-1 not in num_set:
            cur_len=1
            while num+1 in num_set:
                num+=1
                cur_len+=1
            longest_length=max(longest_length,cur_len)
    return longest_length




print(longestConsecutiveSeq2([3, 8, 5, 7, 6]))

# # Time complexity:  O(N) + O(2*N) ~ O(3*N), where N = size of the array.
# Reason: O(N) for putting all the elements into the set data structure. After that for every starting element, we are finding the consecutive elements. Though we are using nested loops, the set will be traversed at most twice in the worst case. So, the time complexity is O(2*N) instead of O(N2).
# Space Complexity: O(N)