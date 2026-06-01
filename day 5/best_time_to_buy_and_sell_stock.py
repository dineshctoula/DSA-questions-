# Question: Best Time to Buy and Sell Stock (LeetCode 121)
# Given an array prices where prices[i] is the price of a given stock on the i-th day.
# Find the maximum profit you can achieve. You cannot sell a stock before you buy one.

# Time Complexity: O(n) - Single pass
# Space Complexity: O(1) - Constant space
def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update minimum price seen so far
        if price < min_price:
            min_price = price
        
        # Calculate profit if sold today and update max_profit
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit

# Test cases
prices = [7, 1, 5, 3, 6, 4]
print("Prices:", prices)
print("Max Profit:", max_profit(prices))