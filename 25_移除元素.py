# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
class Solution(object):
    def removeElement(self, nums: list, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 如果右指针指向的元素不等于 val，它一定是输出数组的一个元素，
        # 我们就将右指针指向的元素复制到左指针位置，然后将左右指针同时右移；
        # 如果右指针指向的元素等于 val，它不能在输出数组里，此时左指针不动，右指针右移一位。
        length = len(nums)
        start = end = 0
        while end < length:
            if nums[end] != val:
                nums[start] = nums[end]
                start += 1
                end += 1
            else:
                end +=1
        return start


if __name__ == '__main__':
    print(Solution().removeElement([3, 2, 2, 3], 3))
