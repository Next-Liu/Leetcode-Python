class Solution(object):
    def traceback(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n + 1):
            path.append(i)
            self.traceback(n, k, i + 1, path, result)
            path.pop()
        return result

    def combine(self, n, k):
        """
        :type n: int
        :type k: int  
        :rtype: List[List[int]]
        """
        res = self.traceback(n, k, 1, [], [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
    # n, m, a, b = map(int, input().split())
    # matrix = []
    # for i in range(n):
    #     matrix.append(list(map(int, input().split())))
    # print(matrix)