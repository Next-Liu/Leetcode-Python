# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
# # 如果 needle 不是 haystack 的一部分，则返回  -1 。

# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        elif needle == '':
            return 0
        else:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle[:]:
                    return i


if __name__ == '__main__':
    print(Solution().strStr("sadbutsad", "but"))
