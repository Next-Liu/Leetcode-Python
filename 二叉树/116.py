# 该二叉树是完全二叉树
from collections import deque


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        root.next = None
        res = root
        q = deque()
        q.append(root)
        i = j = 0
        while q:
            while j < 2 ** i:
                temp = q.popleft()
                if j == 2 ** i - 1:
                    temp.next = None
                else:
                    temp.next = q[0]
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                j += 1
            j = 0
            i += 1
        return res
