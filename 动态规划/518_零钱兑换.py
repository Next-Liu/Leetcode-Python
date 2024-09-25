# 给你一个整数数组coins表示不同面额的硬币，另给一个整数amount表示总金额。
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回0。
# 假设每一种面额的硬币有无限个。题目数据保证结果符合32位带符号整数。
# 本题是求排列数
# 示例1：
# 输入：amount = 5, coins = [1, 2, 5]
# 输出：4
# 解释：有四种方式可以凑成总金额：
# 5 = 5
# 5 = 2 + 2 + 1
# 5 = 2 + 1 + 1 + 1
# 5 = 1 + 1 + 1 + 1 + 1
# 示例2：
# 输入：amount = 3, coins = [2]
# 输出：0
# 解释：只用面额2的硬币不能凑成总金额3。
# 示例3：
# 输入：amount = 10, coins = [10]
# 输出：1
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp[j]：凑成总金额j的货币组合数为dp[j]
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1, 1):
                dp[j] += dp[j-coins[i]]
        return dp[amount]
