def maxProfit(prices):

    min_price = prices[0]
    max_profit = 0

    for price in prices:

        # Update minimum buying price
        if price < min_price:
            min_price = price

        # Current profit
        profit = price - min_price

        # Update maximum profit
        if profit > max_profit:
            max_profit = profit

    return max_profit


# Test
print(maxProfit([7,1,5,3,6,4]))