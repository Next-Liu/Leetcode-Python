class Solution(object):
    def check(self, s, start, end):
        return s[start:end] == s[start:end][::-1]

    def traceback(self, s, startIndex, temp, res):
        if startIndex == len(s):
            res.append(temp[:]) # 这里不能直接append(temp),因为temp是一个引用，后面会改变，所以要append(temp[:])
            return
        for i in range(startIndex, len(s)):
            if self.check(s, startIndex, i+1):
                temp.append(s[startIndex:i + 1])
            else:
                continue
            self.traceback(s, i + 1, temp, res)
            temp.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.traceback(s, 0, [], result)
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.partition('aab')
    print(res)