# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
# 请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]]
# （若两个四元组元素一一对应，则认为两个四元组重复）：
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
class Solution:
    def fourSum(self, nums: list[int], target: int):
        nums.sort()
        ans = []
        tmp_list = []
        if len(nums) < 4:
            return []
        elif len(nums) > 3:
            for i in range(0, len(nums) - 3):
                for j in range(i + 1, len(nums)):
                    left = j + 1
                    right = len(nums) - 1
                    while left < right:
                        if nums[j] + nums[left] + nums[right] + nums[i] > target:
                            right -= 1
                        elif nums[j] + nums[left] + nums[right] + nums[i] < target:
                            left += 1
                        else:
                            tmp_list.append(nums[i])
                            tmp_list.append(nums[j])
                            tmp_list.append(nums[left])
                            tmp_list.append(nums[right])
                            ans.append(tmp_list)
                            tmp_list = []
                            left += 1
                            right -= 1
            ans = list(set([tuple(t) for t in ans]))
            return ans


if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 1))
