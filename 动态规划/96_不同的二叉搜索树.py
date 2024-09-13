class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        if n <= 1:
            return dp[n]
        else:
            # 主要思路：确定树根节点，然后根据左右子树节点个数分别能够组成的二叉树个数，然后相乘
            for i in range(2, n + 1):
                for j in range(1, i+1):
                    dp[i] += dp[j - 1] * dp[i - j]
            return dp[n]


if __name__ == '__main__':
    s = Solution().numTrees(4)
    print(s)
