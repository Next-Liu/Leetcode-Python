class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。找出任意一个 峰值 mat[i][j] 并 返回其位置 [i,j] 。
        假设整个矩阵周边环绕着一圈值为 -1 的格子。
        输入: mat = [[1,4],[3,2]]
        输出: [0,1]
        -1 -1 -1 -1
        -1  1  4 -1
        -1  2  3 -1
        -1 -1 -1 -1
        如果 mat[i] 的最大值比它下面的相邻数字小，则存在一个峰顶，其行号大于 i。缩小二分范围，更新二分区间左端点 left。
        如果 mat[i] 的最大值比它下面的相邻数字大，则存在一个峰顶，从该位置出发的递增路径只能向上走才能走到峰顶
        其行号小于或等于 i。缩小二分范围，更新二分区间右端点 right。
        """
        left, right = 0, len(mat) - 2
        while left <= right:
            mid = (left + right) // 2
            rowMax = max(mat[mid])
            if rowMax > mat[mid + 1][mat[mid].index(rowMax)]:
                right = mid - 1
            else:
                left = mid + 1
        return [left, mat[left].index(max(mat[left]))]
