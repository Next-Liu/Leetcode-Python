class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 判断ransomNote中的字符是否都在magazine中,magazine中的字符只能用一次
        dict1 = {}
        for i in ransomNote:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for j in magazine:
            if j in dict1:
                dict1[j] -= 1
        for k in dict1:
            if dict1[k] > 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canConstruct("aa", "aab"))
