# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
from collections import deque


class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.appendleft(x)


    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        else:
            ans = self.queue.popleft()
            self.queue.appendleft(ans)
            return ans


    def empty(self):
        """
        :rtype: bool
        """
        if self.queue:
            return False
        else:
            return True

if __name__ == '__main__':
    q = deque()
    q.append(1)
    q.append(2)
    q.appendleft(3)
    print(q)