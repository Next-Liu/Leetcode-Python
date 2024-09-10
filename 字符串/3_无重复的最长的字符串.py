class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        length = 0
        temp_length = []
        d = dict()
        for i in range(len(s)):
            for k in range(i, len(s)):
                if d.get(s[k]):
                    d.clear()
                    temp_length.append(length)
                    length = 0
                    break
                else:
                    d[s[k]] = True
                    length += 1
        max_length = temp_length[0]
        for j in range(1, len(temp_length)):
            if temp_length[j] > max_length:
                max_length = temp_length[j]
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("aa"))
