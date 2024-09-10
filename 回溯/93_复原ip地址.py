class Solution(object):
    def traceback(self, s, startIndex, temp, result):
        if startIndex == len(s):
            result.append(temp[:])
        for i in range(startIndex, len(s)):
            temp.append(s[startIndex:i + 1])
            self.traceback(s, i + 1, temp, result)
            temp.pop()

    def check(self, l):
        if len(l) != 4:
            return False
        for i in range(4):
            if len(l[i]) != 1 and l[i][0] == '0':
                return False
            if int(l[i]) > 255:
                return False
        return True

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []  # 用来存储所有的分割结果
        res = []  # 用来存储最终的结果
        self.traceback(s, 0, [], result)
        for i in result:
            if self.check(i):
                res.append(".".join(i))
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.restoreIpAddresses("25525511135")
    print(res)
