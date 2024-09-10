# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 返回这三个数的和。
# 假定每组输入只存在恰好一个解。
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)
class Solution:
    def threeSumClosest(self, nums: list[int], target: int):
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if abs(sum - target) < abs(ans - target):
                    ans = sum
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return target
        return ans


if __name__ == '__main__':
    l = [1, 1, 1, 0]
    target = 100
    print(Solution().threeSumClosest(l, target))
