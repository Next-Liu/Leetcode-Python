# 有一堆石头，每块石头的重量都是正整数。
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
# 示例：
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
# 提示：
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

# 和416题一样，本质是尽量把剩下的石头分成两堆，两堆重量差最小
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        dp = 15001 * [0]
        total = 0
        for stone in stones:
            total += stone
        target = total // 2
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
        return abs(total - 2 * dp[target])  # 最后两堆石头重量分别为dp[target]、total-dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
