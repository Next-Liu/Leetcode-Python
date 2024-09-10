# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# nums是单调递增的
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None:
            return [-1, -1]

        # 找左边界：该位置为target；左边元素小于该位置的元素
        def searchLeft(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    if nums[mid - 1] < nums[mid] or mid == 0:
                        return mid
                    else:
                        r = mid - 1
            return -1

        def searchRight(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    if mid == (len(nums) - 1) or nums[mid + 1] > nums[mid]:
                        return mid
                    else:
                        l = mid + 1
            return -1

        return [searchLeft(nums, target), searchRight(nums, target)]


if __name__ == '__main__':
    print(Solution().searchRange([1], 1))
