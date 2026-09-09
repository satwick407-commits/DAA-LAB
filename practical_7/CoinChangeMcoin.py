class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[amount] == amount + 1:
            return -1

        return dp[amount]


coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

obj = Solution()
result = obj.coinChange(coins, amount)

print("Minimum number of coins:", result)