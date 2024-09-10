# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def traversal(self, root1, root2):
        if root1 is None and root2 is None:
            return None
        if root2 is None:
            return root1
        if root1 is None:
            return root2
        root1.val += root2.val
        root1.left = self.traversal(root1.left, root2.left)
        root1.right = self.traversal(root1.right, root2.right)
        return root1

    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        res = self.traversal(root1, root2)
        return res