class Solution(object):
    def binarySearch(self, nums, target):
        # 左闭右闭区间
        left = 0
        right = len(nums) - 1
        while (left <= right):  # 集合有元素
            mid = left + (right - left) // 2  # 防止溢出
            if nums[mid] >= target:  # 为了让left指向数组中target第一个出现的位置，要保证left左边的数都小于target
                # 故当nums[mid]=target时要让right = mid - 1而不是left = mid + 1
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.binarySearch(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.binarySearch(nums, target + 1) - 1
        return [start, end]
