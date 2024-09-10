class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 查找haystack字符串中是否有子串needle
        # 1.构建next数组
        next = list()
        next.append(0)
        next.append(1)
        n_list = list(needle)
        for j in range(2, len(n_list)):
            child_len = 0
            start = 0
            end = j - 1
            while start < end:
                if n_list[start] == n_list[end]:
                    child_len += 1
                    start += 1
                    end -= 1
                else:
                    break
            next.append(child_len + 1)
        for i in haystack:
            start = i




if __name__ == '__main__':
    print(Solution().strStr("sss", "aabaaf"))
