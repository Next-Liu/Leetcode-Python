class Solution(object):
    def getMax(self, nums, left, right):
        max = nums[left]
        for i in range(left, right):
            if nums[i] > max:
                max = nums[i]
        return max

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums)-k+1):
            max = self.getMax(nums, i, i + k)
            res.append(max)
        return res


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))