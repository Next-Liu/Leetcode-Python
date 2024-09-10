class Solution(object):
    def removeElement(self, nums: list, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fast = low = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[low] = nums[fast]
                low += 1
            fast += 1
        return low
