class Solution(object):
    def checkIp(self, temp_res):
        if len(temp_res) != 4:
            return False
        for i in range(4):
            if len(temp_res[i]) != 1 and temp_res[i][0] == '0':  # 不能以0开头,可以是0，但不能是01,001
                return False
            if int(temp_res[i]) > 255:
                return False
        return True

    def traceback(self, s, startIndex, temp, result):
        if startIndex == len(s):
            result.append(temp[:])
        for i in range(startIndex, len(s)):
            temp.append(s[startIndex:i + 1])
            self.traceback(s, i + 1, temp, result)
            temp.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []  # 用来存储所有的分割结果
        self.traceback(s, 0, [], result)
        res_final = []  # 存储最终结果
        for i in range(len(result)):
            if self.checkIp(result[i]):
                res_final.append(".".join(result[i]))
        return res_final


if __name__ == '__main__':
    s = Solution()
    res = s.restoreIpAddresses("25525511135")
    print(res)
