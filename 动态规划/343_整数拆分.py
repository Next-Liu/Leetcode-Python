# 给定一个正整数n ，将其拆分为k个正整数的和（ k >= 2 ），并使这些整数的乘积最大化。
# 返回你可以获得的最大乘积 。
#
# 示例
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 示例
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                # 一个是j * (i - j)直接相乘。
                # 一个是j * dp[i - j]，相当于是拆分(i - j)
                temp_max = max(j * (i - j), j * dp[i - j])
                dp[i] = max(dp[i], temp_max)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(10))