def knapsack_dp(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    w = capacity
    selection = [0] * n

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selection[i - 1] = 1
            w = w - weights[i - 1]

    return dp[n][capacity], selection


weights = [2, 3, 4, 5]
values = [1, 2, 5, 6]
capacity = 8

maximum_value, selection = knapsack_dp(weights, values, capacity)

print("Maximum Value:", maximum_value)
print("0/1 Selection:", selection)