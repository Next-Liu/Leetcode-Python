# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 输入: num = 58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.

# 输入: num = 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
class Solution:
    def intToRoman(self, num):
        mydict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        if num in mydict.keys():
            return mydict[num]
        res = ''
        while num > 0:
            if num >= 1000:
                res += 'M'
                num -= 1000
            elif num >= 900:
                res += 'CM'
                num -= 900
            elif num >= 500:
                res += 'D'
                num -= 500
            elif num >= 400:
                res += 'CD'
                num -= 400
            elif num >= 100:
                res += 'C'
                num -= 100
            elif num >= 90:
                res += 'XC'
                num -= 90
            elif num >= 50:
                res += 'L'
                num -= 50
            elif num >= 40:
                res += 'XL'
                num -= 40
            elif num >= 10:
                res += 'X'
                num -= 10
            elif num >= 9:
                res += 'IX'
                num -= 9
            elif num >= 5:
                res += 'V'
                num -= 5
            elif num >= 4:
                res += 'IV'
                num -= 4
            elif num >= 1:
                res += 'I'
                num -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(2000))

