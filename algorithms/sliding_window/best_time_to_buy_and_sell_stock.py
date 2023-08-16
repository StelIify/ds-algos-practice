# Given an array where the element at the index i represents the price of a stock on day i,
# find the maximum profit that you can gain by buying the stock once and then selling it.
# Note: Stock can only be purchased on a single day and sold on a different day.
# If no profit can be achieved, we return zero.

def max_profit(stock_prices):
    max_pr = 0
    buy = 0
    for sell in range(1, len(stock_prices)):
        if stock_prices[sell] > stock_prices[buy]:
            current = stock_prices[sell] - stock_prices[buy]
            if current > max_pr:
                max_pr = current
        else:
            buy = sell
    return max_pr


test = [4, 10, 5, 1, 6, 7]
test2 = [7, 1, 5, 3, 6, 4]
print(max_profit(test2))  # 5
