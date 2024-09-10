class Solution(object):
    def swap(self, matrix, i, j):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        matrix : n*n
        """
        n = len(matrix)
        # 转置
        for i in range(n):
            for j in range(i + 1, n):   
                self.swap(matrix, i, j)
        # n=3 交换1和3列
        # n=4 交换1和4列，2和3列 
        count = 0
        while count < (n // 2):
            for j in range(n):
                matrix[j][count], matrix[j][n - 1 - count] = matrix[j][n - 1 - count], matrix[j][count]
            count += 1
        return matrix


if __name__ == '__main__':
    s = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(s.rotate(matrix))
