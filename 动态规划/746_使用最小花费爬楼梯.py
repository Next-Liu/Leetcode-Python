class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp[i]表示到达第i层所需要的最小花费，
        # dp[i] 可以从 dp[i-1] 和 dp[i-2] 转移过来，即 dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        if len(cost) == 2:
            return min(cost)
        dp = [0] * (len(cost) + 1)  # 要爬上最后一层，故长度为len(cost)+1，即求爬到多出来的那一层的最小花费
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]
