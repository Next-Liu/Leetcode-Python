# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getLeft(self, root):
        if root.left is None:
            return root
        else:
            return self.getLeft(root.left)

    def getRight(self, root):
        if root.right is None:
            return root
        else:
            return self.getRight(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.right and root.right.val <= root.val:
            return False
        if root.left and root.left.val >= root.val:
            return False
        if root.right and self.getLeft(root.right).val <= root.val:
            return False
        if root.left and self.getRight(root.left).val >= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)