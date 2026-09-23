INF = float('inf')


def coin_change(coins, amount):
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == INF:
        return -1

    return dp[amount]


def main():
    coins = list(map(int, input("Enter coin values: ").split()))
    amount = int(input("Enter amount: "))

    ans = coin_change(coins, amount)

    if ans == -1:
        print("Change cannot be made.")
    else:
        print("Minimum Coins Required =", ans)


if __name__ == "__main__":
    main()