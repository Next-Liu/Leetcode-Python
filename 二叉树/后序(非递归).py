class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []
        #  后序非递归的思路：通过前序受到启发：根左右->根右左->左右根
        stack = []
        res = []
        stack.append(root)
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return res[::-1]
