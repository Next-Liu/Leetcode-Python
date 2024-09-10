class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 窗口的起始位置如何移动：如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）。
        # 窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，也就是for循环里的索引。
        min_len = float("inf")
        i = 0  # 滑动窗口的左边界
        temp_sum = 0  # 滑动窗口的和
        for j in range(len(nums)):  # 滑动窗口的右边界
            temp_sum += nums[j]
            while temp_sum >= target:
                min_len = min(min_len, j - i + 1)
                temp_sum -= nums[i]  # 左边界向右移动
                i += 1
        return min_len if min_len != float("inf") else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
