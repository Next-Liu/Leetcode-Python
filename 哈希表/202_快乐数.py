class Solution(object):
    def getSum(self, n):
        sum = 0
        while n != 0:
            sum += (n % 10) ** 2
            n = n // 10
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = set()
        sum = self.getSum(n)
        while sum != 1:
            if sum not in res:
                res.add(sum)
            else:
                return False
            sum = self.getSum(sum)
        return True


if __name__ == '__main__':
    print(Solution().isHappy(19))
