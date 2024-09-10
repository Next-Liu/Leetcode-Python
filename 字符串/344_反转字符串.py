class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]  # s[:]是为了修改原数组，而不是新建一个数组


if __name__ == '__main__':
    s = ['h', 'e', 'l', 'l', 'o']
    Solution().reverseString(s)
    print(s)
