# 给你一个由不同整数组成的数组nums ，和一个目标整数target 。请你从nums中找出并返回总和为target的元素组合的个数。
# 题目数据保证答案符合32位整数范围。
# 示例1：
#
# 输入：nums = [1, 2, 3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
# 示例2：
#
# 输入：nums = [9], target = 3
# 输出：0

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(1, target + 1, 1):
            for num in nums:
                if j >= num:
                    dp[j] += dp[j - num]
        return dp[target]
