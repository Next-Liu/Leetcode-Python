# L     C    res[0] = [L, C]
# E  T  O    res[1] = [E, T, O]
# E     D    res[2] = [E, D]
class Solution:
    def convert(self, s: str, numRows):
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
