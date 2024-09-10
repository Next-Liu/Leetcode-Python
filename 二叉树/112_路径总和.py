# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def traversal(self, root, target):
        if root.left is None and root.right is None and target == 0:
            return True
        if root.left is None and root.right is None:
            return False
        if root.left:
            target -= root.left.val
            if self.traversal(root.left, target):
                return True
            target += root.left.val
        if root.right:
            target -= root.right.val
            if self.traversal(root.right, target):
                return True
            target += root.right.val
        return False


    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        res = self.traversal(root,targetSum-root.val)
        return res
