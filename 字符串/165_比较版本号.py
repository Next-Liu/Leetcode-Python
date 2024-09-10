class Solution(object):
    def clearFirstZeros(self, s):
        for i in range(len(s)):
            if s[i] == '0':
                continue
            else:
                return int(s[i:])
        return 0

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        for i in range(min(len(version1), len(version2))):
            if self.clearFirstZeros(version1[i]) > self.clearFirstZeros(version2[i]):
                return 1
            if self.clearFirstZeros(version1[i]) < self.clearFirstZeros(version2[i]):
                return -1
        if len(version1) > len(version2):
            gap = len(version1) - len(version2)
            for i in range(gap):
                if self.clearFirstZeros(version1[len(version1) - 1 - i]) != 0:
                    return 1
        if len(version1) < len(version2):
            gap = len(version2) - len(version1)
            for i in range(gap):
                if self.clearFirstZeros(version2[len(version2) - 1 - i]) != 0:
                    return -1
        return 0


if __name__ == '__main__':
    c = Solution()
    print(c.compareVersion('1.2', '1.10'))
