# 使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）
#  1. 该函数首先根据需要丢弃任意多的空格字符，直到找到第一个非空格字符为止。
#  2. 检查下一个字符是否为可选的正号或负号，没有则将其置为正号。
class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "" or s == "":
            return 0
        digits = [char for char in s if char.isdigit()]
        if len(digits) == 0:
            return 0
        new_s = s.strip()
        sample = 0  # 用于记录整数的正负
        if new_s[0] == '-':
            sample = 1
            new_s = new_s[1:]
        elif new_s[0] == '+':
            new_s = new_s[1:]
        new_s = new_s.lstrip('0')
        start = end = j = 0
        for i in range(len(new_s)):
            if new_s[i].isdecimal():
                start = end = j = i
                break
        while j < len(new_s):
            if new_s[j].isdecimal():
                end += 1
                j += 1
            else:
                break

        new_s = new_s[start:end]
        res = int(new_s)
        if sample == 0:
            if res <= 2 ** 31 - 1:
                return res
            else:
                return 2 ** 31 - 1
        else:
            if -res < -2 ** 31:
                return -2 ** 31
            else:
                return -res


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("words and 897   "))
