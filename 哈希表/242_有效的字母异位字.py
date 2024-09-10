# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        for i in s:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in t:
            if i not in dict2:
                dict2[i] = 1
            else:
                dict2[i] += 1
        return dict1 == dict2


if __name__ == '__main__':
    # print(Solution().isAnagram("anagram", "angaram"))
    # print(Solution().isAnagram("rat", "car"))
    print(Solution().isAnagram("aa", "a"))
