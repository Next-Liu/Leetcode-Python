# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
# 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
