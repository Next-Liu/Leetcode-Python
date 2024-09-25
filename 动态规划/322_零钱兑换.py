# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1
# 你可以认为每种硬币的数量是无限的。
# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
# 输入：coins = [2], amount = 3
# 输出：-1
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        temp_min = float('inf')
        # float('-inf')
        # java表示：
        # 正无穷：Double.POSITIVE_INFINITY
        # 负无穷：Double.NEGATIVE_INFINITY
        dp = [0] * (amount + 1)  # dp[i]代表使用coins中的硬币组合成总量为i的最小个数，所以加的时候要加每一轮dp[i - coins[j]]的最小值
        for i in range(1, amount + 1, 1):
            for j in range(len(coins)):
                if i >= coins[j] and temp_min > dp[i - coins[j]]:
                    temp_min = dp[i - coins[j]]
            dp[i] = temp_min + 1
            temp_min = float('inf')
        return dp[amount] if dp[amount] != float('inf') else -1
