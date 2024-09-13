n, totalWeight = map(int, input().split())
weight = list(map(int, input().split()))
value = list(map(int, input().split()))
dp = [[0] * (totalWeight + 1) for _ in range(n)]
for j in range(weight[0], totalWeight + 1):
    # 初始化dp数组
    dp[0][j] = value[0]

# dp[i][j]:i表示物品，j表示背包容量，dp[i][j]表示从下标0-i的物品取，背包容量为j时所能装物品的最大价值
# 按行遍历
for i in range(1, n):
    for j in range(totalWeight + 1):
        if j < weight[i]:  # 背包容量不够  如果改成j<weight[i]+weight[i-1]会损失掉当要装的物品的重量=j且价值更高时，应该只装物品i
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
print(dp[n - 1][totalWeight])
