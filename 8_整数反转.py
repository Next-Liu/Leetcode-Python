# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围[−2^31,2^31− 1] ，就返回 0。
# 输入：x = 123
# 输出：321
# 输入：x = 120
# 输出：21
# 输入：x = -123
# 输出：-321

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            x = list(str(x)[1:])
            x.reverse()
            x = -int("".join(x))
            if x < -2 ** 31:
                return 0
            else:
                return x
        else:
            x = list(str(x))
            x.reverse()
            x = int("".join(x))
            if x > 2 ** 31 - 1:
                return 0
            else:
                return x


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(153))
