class Solution:
    def longestPalindrome(s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        if n < 2:
            return s
        start, max_len = 0, 1
        for right in range(n):
            for left in range(0, right + 1):
                '''
                (0) 求子串跨越长度span
                (1) 边缘情况1: 子串长度为1, 则一定是回文
                (2) 边缘情况2: 子串长度为2, 如果俩字符相同则是回文
                (3) 非边缘情况则进行动态规划之状态转移: 如果b是回文, aba也一定是回文
                    即判断是否为回文需同时满足两条件: 
                        1. 剥离左右最外层字符后的子字符串是回文 
                        2. 最外层的字符相同
                '''
                child_len = right - left + 1
                if child_len == 1:
                    dp[left][right] = True
                elif child_len == 2:
                    dp[left][right] = s[left] == s[right]
                else:
                    dp[left][right] = dp[left + 1][right - 1] and s[left] == s[right]
                if dp[left][right]:
                    if child_len > max_len:
                        max_len = child_len
                        start = left
        return s[start:start + max_len]


if __name__ == '__main__':
    s = 'abcbcbcbcbc'
    print(Solution.longestPalindrome(s))
