class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        left = 0
        length = len(nums)
        prod = 1
        ans = 0
        for i in range(length):
            prod *= nums[i]
            while prod >= k:  # 乘积>=k就不断缩小窗口，左指针右移
                prod /= nums[left]
                left += 1
            ans += i - left + 1
        return ans
