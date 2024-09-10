from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            len_q = len(q)
            for i in range(len_q):
                temp = q.pop()
                if i == len_q - 1:
                    res.append(temp.val)
                if temp.left:
                    q.appendleft(temp.left)
                if temp.right:
                    q.appendleft(temp.right)
        return res
