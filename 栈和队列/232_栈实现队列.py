# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
class MyQueue(object):

    def __init__(self):
        self.stack_in = []   # 入队列 1 2 3
        self.stack_out = []  # 出队列 3 2 1 pop()的顺序是 1 2 3

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack_in or self.stack_out:
            return False
        else:
            return True

if __name__ == '__main__':
    l = []
    l.append(1)
    l.append(2)
    l.append(3)
    print(l)
    print(l.pop())
    print(l)