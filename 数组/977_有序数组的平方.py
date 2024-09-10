# 给你一个按非递减顺序排序的整数数组nums，返回每个数字的平方组成的新数组，要求也按
# 非递减顺序排序。
# 示例1：
#
# 输入：nums = [-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
#
# 示例2：
#
# 输入：nums = [-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 使用双指针法,最大值一定在两端
        left, right = 0, len(nums) - 1
        ans = [0] * len(nums)
        k = len(nums) - 1
        while k >= 0:
            if nums[left] ** 2 < nums[right] ** 2:
                ans[k] = nums[right] ** 2
                k -= 1
                right -= 1
            elif nums[left] ** 2 > nums[right] ** 2:
                ans[k] = nums[left] ** 2
                k -= 1
                left += 1
            else:
                ans[k] = nums[left] ** 2
                if k >= 1:
                    ans[k - 1] = nums[left] ** 2
                left += 1
                right -= 1
                k -= 2
        return ans


if __name__ == '__main__':
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
