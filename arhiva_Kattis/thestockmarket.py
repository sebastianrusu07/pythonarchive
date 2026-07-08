n = int(input())
k = int(input())

prices = []
for i in range(n):
    prices.append(int(input()))

biggestProfit = -1
for i in range(0,n-k):
    buy = prices[i]
    sell = prices[i+k]
    profit = sell - buy
    if biggestProfit == -1 or profit > biggestProfit:
        biggestProfit = profit

print(biggestProfit)