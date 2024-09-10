class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = right = 0
        if root.left:
            left = self.maxDepth(root.left)
        if root.right:
            right = self.maxDepth(root.right)
        return max(left, right) + 1
