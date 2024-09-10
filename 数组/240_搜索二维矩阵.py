class Solution(object):
    # 矩阵特性
    # 每行的元素从左到右升序排列。
    # 每列的元素从上到下升序排列。
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            for j in range(len(row)):
                if row[j] == target:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    print(s.searchMatrix(matrix, 20))
