class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        原数组中可能有重复的元素，旋转n次返回数组中的最小元素
         [3,1,3]
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]