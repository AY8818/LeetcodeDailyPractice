import math


def coinChange(coins, amount):
    lst = [math.inf] * (amount + 1)
    lst[0] = 0
    print(lst)
    for coin in coins:
        print("current coin = ", coin)
        for i in range(coin, amount + 1):
            print("i = ", i)
            print(f"\nif {i - coin} >= 0 {i - coin >= 0}")
            if i - coin >= 0:
                lst[i] = min(lst[i], lst[i - coin] + 1)
                print(lst)
    return -1 if lst[-1] == math.inf else lst[-1]


coins = [1, 2, 5]

amount = 11
print(coinChange(coins, amount))
