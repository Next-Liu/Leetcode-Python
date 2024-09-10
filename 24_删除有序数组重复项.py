# 给你一个升序排列的数组 nums ，请你原地删除重复出现的元素，使每个元素只出现一次 ，
# 返回删除后数组的新长度。元素的相对顺序应该保持一致 。然后返回 nums 中唯一元素的个数。
# 考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
# 更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
# 返回 k 。
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        start = 0
        end = 1
        while end < len(nums):
            if nums[end] == nums[start]:
                del nums[end]
                end = start + 1
            else:
                start = end
                end = start + 1
        return len(nums)


if __name__ == '__main__':
    print(Solution().removeDuplicates([0, 0, 1, 1, 2, 2, 3, 5]))
