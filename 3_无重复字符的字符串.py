# 输入: s = "abcabcbb"
# 输出: 3
class Solution(object):
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        all_len = []
        if s == " ":
            return 1
        elif s == "":
            return 0
        else:
            for i in range(len(s)):
                if s[i] not in result:
                    result.append(s[i])
                else:
                    all_len.append(len(result))
                    index = result.index(s[i])
                    result = result[index + 1:]
                    result.append(s[i])
            all_len.append(len(result))

        return max(all_len)


if __name__ == '__main__':
    len = Solution.lengthOfLongestSubstring("c")
    print(len)
