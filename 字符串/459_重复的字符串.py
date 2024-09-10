class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 检测s是否可以由他的一个子串重复构成
        # 若s = abcabc   s+s=abc abcabc abc（中间还出现了个s）
        # 若s = aab      s+s=aabaab
        t = s + s
        l = list(t)
        t_l = list(s)
        for i in range(1, len(l) - len(s)):  # 掐头去尾
            if l[i:i + len(s)] == t_l:
                return True
        return False
