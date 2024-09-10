# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
# 1<=n<=8
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        m = n * 2
        ans = []
        path = [''] * m

        def dfs(i, open):  #open代表左括号个数
            if i == m:
                ans.append(''.join(path))
                return
            if open < n:
                path[i] = '('
                dfs(i + 1, open + 1)
            if i - open < open:
                path[i] = ')'
                dfs(i + 1, open)

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
