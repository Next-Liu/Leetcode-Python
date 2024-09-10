class Solution(object):
    # 计算一个矩阵中的最大和最小值
    def getMaxAndMin(self, matrix, row, col):
        min = matrix[0][0]
        max = matrix[row - 1][col - 1]
        return min, max


if __name__ == '__main__':
    n, m, a, b = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    row_matrix = []
    temp_row_matrix = []
    for element in matrix:
        for i in range(len(element) - b + 1):
            temp_row_matrix.append(element[i:i + b])
        row_matrix.append(temp_row_matrix)
        temp_row_matrix = []
    temp_matrix = []
    temp_sum = 0
    count = 0
    for k in range(a):
        for ele in row_matrix:
            temp_matrix.append(ele[k])
            count += 1
            if count == a:
                small, big = Solution().getMaxAndMin(temp_matrix, a, b)
                temp_sum += small*big
                count = 0
                temp_matrix = []
                break
    print(temp_sum)
    print(row_matrix)

