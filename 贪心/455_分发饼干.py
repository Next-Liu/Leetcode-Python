# 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；
# 并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
# 你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
class Solution(object):
    def findContentChildren(self, g: list, s: list):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        g.sort()
        s.sort()
        j = 0
        for i in s:
            while j < len(g):
                if i >= g[j]:
                    j += 1
                    count += 1
                    break  # 遇到满足的就应该直接跳出，不应该重复使用
                else:
                    break
        return count
