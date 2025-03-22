# Stock Buy And Sell


# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input:
#  prices = [7,1,5,3,6,4]
# Output:
#  5


# Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


# Approach :1

def stockBuySell1(arr):
    max_profit=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            max_profit=max(max_profit,arr[j]-arr[i])
    return max_profit

print(stockBuySell1([7,6,4,3,1]))

# Time Complexity: O(N^2)
# Space COmplexity: O(1)



# ---------------------------------------------------------------

# Approach:2 (Optimal Solution)

def stockBuySell2(arr):
    max_profit=0
    lowest_price=arr[0]
    for i in range(1,len(arr)):
        lowest_price=min(arr[i],lowest_price)
        max_profit=max(max_profit,arr[i]-lowest_price)
    return max_profit

print(stockBuySell2([7,6,4,3,1]))

# Time Complexity: O(N)
# Space COmplexity: O(1)