class Solution(object):
    def traceback(self, nums, startIndex, temp, res):
        res.append(temp[:])
        for i in range(startIndex, len(nums)):
            temp.append(nums[i])
            self.traceback(nums, i + 1, temp, res)
            temp.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.traceback(nums, 0, [], res)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.subsets([1, 2, 3])
    print(res)
