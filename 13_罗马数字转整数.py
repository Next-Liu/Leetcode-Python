# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
# X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
# C可以放在D(500) 和M(1000) 的左边，来表示400 和900
class Solution:
    def romanToInt(self, s: str):
        mydict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and mydict[s[i]] < mydict[s[i + 1]]:
                res -= mydict[s[i]]
            else:
                res += mydict[s[i]]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))
