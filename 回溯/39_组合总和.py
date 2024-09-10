class Solution(object):
    def traceback(self, candiates, target, sum, startIndex, path, result):
        if sum > target:
            return
        if sum == target:
            result.append(path[:])  # 这里不能直接append(path),因为path是一个引用，后面会改变，所以要append(path[:])
            return
        for i in range(startIndex, len(candiates)):
            sum += candiates[i]
            path.append(candiates[i])
            self.traceback(candiates, target, sum, i, path, result)
            sum -= candiates[i]
            path.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.traceback(candidates, target, 0, 0, [], result)
        return result

if __name__ == '__main__':
    s = Solution()
    res = s.combinationSum([2, 3, 6, 7], 7)
    print(res)
