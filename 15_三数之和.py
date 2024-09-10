# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
# 你返回所有和为 0 且不重复的三元组。
# 输入：nums = [-1,0,1,2,-1,-4]   [-1,-1,0,1,2,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要
class Solution:
    def threeSum(self, nums: list):
        final_list = []
        nums.sort()
        tmp_list = []
        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    tmp_list.append(nums[left])
                    tmp_list.append(nums[right])
                    tmp_list.append(nums[i])
                    final_list.append(tmp_list)
                    tmp_list = []
                    left += 1
                    right -= 1
        final_list = list(set([tuple(t) for t in final_list]))
        return final_list


if __name__ == '__main__':
    print(Solution().threeSum([-2, 0, 1, 1, 2]))
