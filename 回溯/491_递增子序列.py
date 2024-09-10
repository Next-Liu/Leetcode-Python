# 示例 1：
#
# 输入：nums = [4,6,7,7]
# 输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# 示例 2：
#
# 输入：nums = [4,4,3,2,1]
# 输出：[[4,4]]
from collections import deque


class Solution(object):
    def traceback(self, nums, startIndex, temp, result):
        if len(temp) > 1:
            result.append(temp[:])
        #  还需要进行去重
        use_set = set()
        for i in range(startIndex, len(nums)):
            if (temp and temp[-1] > nums[i]) or nums[i] in use_set:
                continue
            use_set.add(nums[i])
            temp.append(nums[i])
            self.traceback(nums, i + 1, temp, result)
            temp.pop()

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.traceback(nums, 0, [], result)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubsequences([4, 6, 7, 7]))
