# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def traversal(self, root, val):
        if root and root.val == val:
            return root
        if root.left:
            l = self.traversal(root.left, val)
            if l:
                return l
        if root.right:
            r = self.traversal(root.right, val)
            if r:
                return r
        return None

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        else:
            res = self.traversal(root, val)
            return res


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    s = Solution()
    res = s.searchBST(root, 5)
    print(res)
