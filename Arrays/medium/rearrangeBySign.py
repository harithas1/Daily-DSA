# Rearrange Array Elements by Sign


# Approach: 1(Brute Force)

def rearrangeBySign(arr):
    pos=[]
    neg=[]
    for num in arr:
        if num<0:
            neg.append(num)
        else:
            pos.append(num)
    for i in range(len(pos)):
        arr[i*2]=pos[i]
    for i in range(len(neg)):
        arr[(2*i)+1]=neg[i]

    
arr=[1,2,-3,-1,-2,3]
rearrangeBySign(arr)
print(arr)


# TIme complexity: O(N+N/2)
# space complexity: O(N/2+N/2)=O(N)

# --------------------------------------------------------------


# Approach: 2(Optimal approach)

def rearrangeBySign2(arr):
    n=len(arr)
    ans=[0]*n
    pI=0
    nI=1
    for i in range(len(arr)):
        if arr[i]>0:
            ans[pI]=arr[i]
            pI+=2
        else:
            ans[nI]=arr[i]
            nI+=2
    return ans

arr=[1,2,-3,-1,-2,3]
print(rearrangeBySign2(arr))

# TIme complexity: O(N)
# space complexity: O(N)

