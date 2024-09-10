class Solution(object):
    def dynamicPassword(self, password, target):
        """
        :type password: str
        :type target: int
        :rtype: str
        """
        l = list(password)
        self.reversed(l, 0, target - 1)
        self.reversed(l, target, len(password) - 1)
        self.reversed(l, 0, len(password) - 1)
        return ''.join(l)

        # 翻转前target个字符
    def reversed(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    print(Solution().dynamicPassword("s3cur1tyC0d3", 4))
