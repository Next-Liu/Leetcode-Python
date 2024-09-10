# 输入：tokens = ["2", "1", "+", "3", "*"]
# 输出：9
# 解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
from collections import deque


class Solution(object):
    def compute(self, x1, x2, t):
        if t == '+':
            return x1 + x2
        elif t == '-':
            return x1 - x2
        elif t == '*':
            return x1 * x2
        elif t == '/':
            return int(x1 / x2)

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operation = deque()
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                operation.append(t)
            else:
                x2 = int(operation.pop())
                x1 = int(operation.pop())
                sum = self.compute(x1, x2, t)
                operation.append(sum)

        return operation.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))