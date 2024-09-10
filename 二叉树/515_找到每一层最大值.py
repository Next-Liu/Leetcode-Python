# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = deque()
        res = []
        q.append(root)
        temp_max = -float('inf')
        while q:
            for _ in range(len(q)):
                temp = q.pop()
                temp_max = temp.val if temp.val > temp_max else temp_max
                if temp.left:
                    q.appendleft(temp.left)
                if temp.right:
                    q.appendleft(temp.right)
            res.append(temp_max)
            temp_max = -float('inf')
        return res
