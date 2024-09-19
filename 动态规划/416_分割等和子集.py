class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp[j]表示 背包总容量（所能装的总重量）是j，放进物品后，背的最大重量为dp[j]，初始化dp数组，长度为sum//2，
        # 那么如果背包容量为target， dp[target]就是装满 背包之后的重量，所以 当 dp[target] == target 的时候，背包就装满了。
        total = 0
        for ele in nums:
            total += ele
        if total % 2 != 0:
            return False
        dp = [0] * 10001
        target = total // 2
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        if dp[target] == target:
            return True
        else:
            return False
