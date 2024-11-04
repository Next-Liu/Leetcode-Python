class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 若旋转4次，则可以得到[4, 5, 6, 7, 0, 1, 2]
        # 若旋转7次，则可以得到[0, 1, 2, 4, 5, 6, 7]
        # 原数组升序，要找到数组中的最小值
        # 设 n = len(nums),旋转x次就把数组分为长度为x和n-x的有序子数组最小值要么在nums[0]，要么在nums[n-x]
        left = 0
        right = len(nums) - 1
        """
            通过比较中间的值和最后一个值，来判断最小值的位置
            1.nums[mid]>nums[-1]
                数组被分成两段，前一段平均值大于后一段，最小值在后一段
            2.nums[mid]<=nums[-1]
                说明此时nums[mid]在后半段，nums[mid]要么是最小值，要么在最小值右边
        """

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[left]


if __name__ == '__main__':
    # 输入一段数字
    nums = [int(x) for x in input().split(" ")]
    print(Solution().findMin(nums))
