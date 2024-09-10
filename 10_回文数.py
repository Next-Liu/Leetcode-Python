# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 输入：x = -121
# 输出：false
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r_s = s[::-1]
        if s == r_s:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isPalindrome(121))
    a = -123
    l = str(a)
    print(l[::-1]) # 字符串反转
