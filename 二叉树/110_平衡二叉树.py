class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if self.Balance(root) != -1 else False

    def Balance(self, root):
        if not root:
            return 0
        left = self.Balance(root.left)
        right = self.Balance(root.right)
        if abs(left - right) > 1 or left == -1 or right == -1:  # 因为这里的left和right也可能代表以某个节点为根节点的子树的深度，所以要判断left和right是否为-1
            return -1
        return max(left, right) + 1
