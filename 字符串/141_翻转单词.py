class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s.split(' '))
        left = 0
        right = len(l) - 1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        res = ' '.join(l)  # join()默认以空格连接
        # 去除多余的空格
        res = ' '.join(res.split()) # split()默认以空格分割
        return res


if __name__ == '__main__':
    s = 'a good   example'
    print(Solution().reverseWords(s))
