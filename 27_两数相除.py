# 给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和取余运算。
# 整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2。
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = 3.33333.. ，向零截断后得到 3
#
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = -2.33333.. ，向零截断后得到 -2 。

# 我们可以把一个dividend（被除数）先除以2^n，n最初为31，不断减小n去试探,当某个n满足dividend/2^n>=divisor时，
# 表示我们找到了一个足够大的数，这个数*divisor是不大于dividend的，所以我们就可以减去2^n个divisor，以此类推
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if dividend >= 0 and divisor > 0:
            flag = 1
        elif dividend < 0 and divisor < 0:
            flag = 1
        else:
            flag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
    # 左移：<< 右移：>>
        for i in range(31, -1, -1):
            if dividend >= divisor << i:
                dividend -= divisor << i
                count += 1 << i
        if flag == 1:
            return min(count, 2**31-1)
        else:
            return max(-count, -2**31)
