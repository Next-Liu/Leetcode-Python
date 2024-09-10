from collections import deque


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 新建一个栈，如果压入的元素与栈顶元素相同，则弹出栈顶元素，否则直接压入
        stack_in = deque()
        stack_out = []
        for i in s:
            if len(stack_in) == 0:
                stack_in.append(i)
            elif i == stack_in[-1]:
                stack_in.pop()
            else:
                stack_in.append(i)
        while stack_in:
            ele = stack_in.pop()
            stack_out.append(ele)
        return ''.join(stack_out[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates('abbaca'))
