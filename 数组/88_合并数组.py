class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 把nums2的元素添加到nums1中
        nums1[m:] = nums2
        length = m + n - 1
        # 对nums1进行快速排序
        self.quickSort(nums1, 0, length)

    def quickSort(self, nums, left, right):
        if left < right:
            pivot = self.getPartion(left, right, nums)
            if pivot > 0:
                self.quickSort(nums, left, pivot - 1)
            self.quickSort(nums, pivot + 1, right)

    def getPartion(self, left, right, nums):
        x = nums[left]
        while (left < right):
            while (nums[right] >= x and left < right):
                right -= 1
            nums[left] = nums[right]
            while (nums[left] <= x and left < right):
                left += 1
            nums[right] = nums[left]
        nums[left] = x
        return left


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)
