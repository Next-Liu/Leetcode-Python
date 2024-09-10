# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 1->2->3
# 8->9->4
# 7<-6<-5
# n = 3
# 输出:
# [[1,2,3],[8,9,4],[7,6,5]]
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0] * n for _ in range(n)]
        #  循环次数为 n/2次 若n为奇数，对中间元素单独赋值
        num, mid = n // 2, n // 2
        startx = 0
        starty = 0
        count = 1
        offset = 1  # 控制边界，每一轮循环不遍历到每一行（列）的最后一个数
        while num > 0:
            for j in range(starty, n - offset):  # 第一轮改变的是列坐标
                ans[startx][j] = count
                count += 1
            for i in range(startx, n - offset):  # 第二轮改变的是横坐标
                ans[i][n - offset] = count
                count += 1
            for j in range(n - offset, starty, -1):  # 从右至左
                ans[n - offset][j] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下至上
                ans[i][starty] = count
                count += 1
            startx += 1
            starty += 1
            offset += 1
            num -= 1
        if n % 2 != 0:
            ans[mid][mid] = n ** 2
        return ans


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
