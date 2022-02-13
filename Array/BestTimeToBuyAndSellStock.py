arr1 = [7,1,5,3,6,4]
arr2 = [7,6,4,3,1]

# first solution 
def maxProfit(prices):
    max_profit = 0
    min_price = float('inf') #infinity 

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# print(maxProfit(arr1))

# second solution: two pointer solution 
def max_Profit(prices):
    max_profit = 0 
    buy = 0 
    sell = 1
    
    while sell < len(prices):
        if prices[buy] < prices[sell]:
           max_profit = max(max_profit, prices[sell] - prices[buy])
        else:
            buy = sell 
        sell += 1
    return max_profit

# print(max_Profit(arr1))