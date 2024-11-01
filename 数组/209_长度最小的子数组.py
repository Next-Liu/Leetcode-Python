# 示例 1：
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        total = 0
        length = len(nums)
        ans = length + 1
        for right in range(length):
            total += nums[right]
            while total - nums[left] >= target:  # 缩小窗口
                total -= nums[left]
                left += 1
            if total >= target:
                ans = min(ans, right - left + 1)
        return ans if ans <= length else 0
