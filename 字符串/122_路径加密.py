class Solution(object):
    def pathEncryption(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = list(path.split(','))
        return " ".join(res)


if __name__ == '__main__':
    path = "a,b,c,d,e,f,g,h"
    print(Solution().pathEncryption(path))
