# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，
# 那么数组的下一个排列就是在这个有序容器中排在它后面的那个排列。
# 如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

# 给定若干个数字，将其组合为一个整数。如何将这些数字重新排列，以得到下一个更大的整数。
# 如 123 下一个更大的数为 132。如果没有更大的整数，则输出最小的整数。

# 必须原地修改，只允许使用额外常数空间。
# 示例 1：

# 输入：nums = [1,2,3]
# 输出：[1,3,2]
# 示例 2：

# 输入：nums = [3,2,1]
# 输出：[1,2,3]
# 示例 3：
# 为了得到下一个序列，需要从后向前查找第一个顺序对 (i,j)，满足 a[i] < a[j]。其中 j 到 n 的子数组是降序的。
# 随后从后向前遍历，找到第一个满足 a[i] < a[k] 的 k。交换 a[i] 与 a[k]，并且反转 j 到 n 的子数组。
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        count = 0
        for q in range(len(nums) - 1):
            if nums[q] >= nums[q + 1]:
                count += 1
                continue
        if count == len(nums) - 1:
            nums.sort()
            return
        end = len(nums) - 1
        i = end - 1
        while i >= 0:
            j = i + 1
            if nums[i] < nums[j]:
                break
            else:
                i -= 1
        for k in range(end, i, -1):
            if nums[k] > nums[i]:
                nums[i], nums[k] = nums[k], nums[i]
                new_nums = nums[i + 1:end + 1][::-1]
                nums[i + 1:end + 1] = new_nums
                break


if __name__ == '__main__':
    nums = [5,1,1]
    Solution().nextPermutation(nums)
    print(nums)
