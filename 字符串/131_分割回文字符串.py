class Solution(object):
    """
    判断字符串是否为回文字符串
    """

    def isPalindrome(self, s, start, end):
        return s[start:end] == s[start:end][::-1]

    """
    :type s: str 字符串
    :type startIndex: int 开始索引
    :type path: List[str] 保存路径
    :type result: List[List[str]] 保存结果
    """

    def traceback(self, s, startIndex, path, result):
        if startIndex == len(s):
            result.append(path[:])
            return
        for i in range(startIndex, len(s)):
            if self.isPalindrome(s, startIndex, i + 1):
                path.append(s[startIndex:i + 1])
            else:
                continue
            self.traceback(s, i + 1, path, result)
            path.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        path = []
        result = []
        self.traceback(s, 0, path, result)
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.partition('aab')
    print(res)
