class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        ans = 0
        cnt = {}
        for right in range(len(s)):
            if cnt.get(s[right]):
                cnt[s[right]] += 1
            else:
                cnt[s[right]] = 1
            while cnt[s[right]] > 1:  # 重复的字符一定来自于新接入的字符abcbbb，左指针向右遍历直到新接入的字符出现次数变为1
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))