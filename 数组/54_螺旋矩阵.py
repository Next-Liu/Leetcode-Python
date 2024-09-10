class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_begin = 0
        row_end = len(matrix[0]) - 1
        column_begin = 0
        column_end = len(matrix) - 1
        ans = []
        while True:
            # 左->右  column_begin > column_end 结束循环
            for i in range(row_begin, row_end + 1):
                ans.append(matrix[column_begin][i])
            column_begin += 1
            if column_begin > column_end:
                break
            # 上->下
            for i in range(column_begin, column_end + 1):
                ans.append(matrix[i][row_end])
            row_end -= 1
            if row_end < row_begin:
                break
            # 界为row_begin-1和column_begin-1是为了不遍历到本轮外层元素
            # 右->左
            for i in range(row_end, row_begin - 1, -1):
                ans.append(matrix[column_end][i])
            column_end -= 1
            if column_end < column_begin:
                break
            # 下->上
            for i in range(column_end, column_begin - 1, -1):
                ans.append(matrix[i][row_begin])
            row_begin += 1
            if row_begin > row_end:
                break
        return ans
