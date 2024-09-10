# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
class Solution:
    def longestCommonPrefix(strs: list):
        if len(strs) == 0:
            return ""
        # 找到最短的字符串
        min_len = len(strs[0])
        min_len_index = 0
        for i in range(1, len(strs)):
            if len(strs[i]) < min_len:
                min_len_index = i
                min_len = len(strs[i])
        if min_len_index != 0:
            strs[0], strs[min_len_index] = strs[min_len_index], strs[0]
        res = strs[0]
        for j in range(1,len(strs)):
            if len(res) == 0:
                return ""
            for k in range(len(res)):
                if strs[j][k] != res[k]:
                    res = res[:k]
                    break
        return res


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution.longestCommonPrefix(strs))
