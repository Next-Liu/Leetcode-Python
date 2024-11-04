class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:  # 数组发生旋转，被分为两段，最小值在后面一段
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        示例 1：
            输入：nums = [4,5,6,7,0,1,2], target = 0
            输出：4
        示例 2：
            输入：nums = [4,5,6,7,0,1,2], target = 3
            输出：-1
        示例 3：
            输入：nums = [1], target = 0
            输出：-1
        使用两次二分差找，第一次找到最小值位置
        第二次：
            if target>nums[len(nums)-1]
                在[0:min-1]二分
            if target <= nums[len(nums)-1]
                在[min:len(nums)]二分
        """
        i = self.findMin(nums)
        if target > nums[len(nums) - 1]:
            res = self.binarySearch(nums, 0, i - 1, target)
        elif target <= nums[len(nums) - 1]:
            res = self.binarySearch(nums, i, len(nums) - 1, target)
        return res if nums[res] == target else -1


if __name__ == '__main__':
    x = [int(x) for x in input().split(" ")]
    target = int(input())
    print(Solution().search(x, target))
