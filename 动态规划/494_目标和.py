# 给你一个非负整数数组nums和一个整数target 。
# 向数组中的每个整数前添加'+'或'-' ，然后串联起所有整数，可以构造一个
# 示例 1：
# 输入：nums = [1, 1, 1, 1, 1], target = 3
# 输出：5
# 解释：一共有5种方法让最终目标和为3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
# 输入：nums = [1], target = 1
# 输出：1

# 提示：
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # left+right =sum left-right = target
        # left = (target+sum)/2
        # 本质找出和为left的组合
        total = 0
        for num in nums:
            total += num
        if abs(target) > total:
            return 0
        if (target + total) % 2 == 1:
            return 0  # 此时没有方案
        left = (total + target) // 2  # 目标和
        dp = [[0] * (left + 1) for _ in range(len(nums) + 1)]  # dp[i][j]代表使用前i个物品在装满容量为j的背包时的方法数
        dp[0][0] = 1  # 装满背包容量为0 的方法数量是1，即放0件物品。
        for k in range(1, len(nums) + 1):
            for q in range(left + 1):
                # 不放物品k：dp[k-1][q]  放物品k：dp[k-1][q-nums[k]] 故dp[k][q] = dp[k-1][q]+dp[k-1][q-nums[k]]
                if nums[k-1] > q:
                    dp[k][q] = dp[k - 1][q]
                else:
                    dp[k][q] = dp[k-1][q]+dp[k-1][q-nums[k-1]]
        return dp[len(nums)][left]