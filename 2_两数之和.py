class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                else:
                    continue
        return result


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    result = Solution.twoSum(nums, target)
    print(result)
