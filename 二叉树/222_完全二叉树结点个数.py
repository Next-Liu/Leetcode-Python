from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = deque()
        q.append(root)
        sum = 1
        while q:
            for _ in range(len(q)):
                temp = q.pop()
                if temp.left:
                    sum += 1
                    q.appendleft(temp.left)
                if temp.right:
                    sum += 1
                    q.appendleft(temp.right)
        return sum
