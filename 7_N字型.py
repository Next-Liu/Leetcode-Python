# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
class Solution:
    def convert(self, s: str, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        res = s[0]
        l = list(s)
        step = 2 * numRows - 2
        i = 0
        for i in range(0, len(l), step):
            if i + step < len(l) and l[i + step] != "":
                res += l[i + step]
                l.pop(i + step)
                l.insert(i + step, "")
        l.pop(0)
        l = [i for i in l if i != ""]
        while step >= 2:
            i = 0
            count = 1
            step -= 2
            res += l[0]
            if step == 0:
                break
            while i < len(l):
                if count % 2 == 1:
                    if i + step < len(l) and l[i + step] != "":
                        res += l[i + step]
                        l.pop(i + step)
                        l.insert(i + step, "")
                        count += 1
                        i += step
                    else:
                        break
                else:
                    if i + 1 < len(l) and l[i + 1] != "":
                        res += l[i + 1]
                        l.pop(i + 1)
                        l.insert(i + 1, "")
                        count += 1
                        i += 1
                    else:
                        break
            l.pop(0)
            l = [k for k in l if k != ""]
        l.pop(0)
        for i in l:
            res += i
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.convert("abcde", 4))
