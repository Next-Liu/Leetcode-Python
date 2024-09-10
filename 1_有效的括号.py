# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        list_i = ['(', '[', '{']
        list_o = [')', ']', '}']
        stack = []
        for i in s:
            if i in list_i:
                stack.append(i)
            elif i in list_o and stack:
                if i == ')' and stack.pop() == '(':
                    continue
                if i == ']' and stack.pop() == '[':
                    continue
                if i == '}' and stack.pop() == '{':
                    continue
                return False
            else:
                return False
        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "()"
    flag = Solution.isValid(s)
    print(flag)
