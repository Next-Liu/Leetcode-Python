class Solution:
    def permute(self, nums):
        result = []
        self.backtracking(nums, [], [False] * len(nums), result)
        return result

    def backtracking(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):  # 不用startIndex，每一轮都用从头开始,递归时返回时，i会自动加1
            if used[i]:   # 如果已经使用过，跳过
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
    n, m, a, b = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(matrix)

