class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 2
        # 通过比较nums[mid]和nums[mid+1]的大小确定封顶的位置
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:  # 峰顶在mid左边
                right = mid - 1
            else:  # 峰顶在mid右边
                left = mid + 1
        return left
