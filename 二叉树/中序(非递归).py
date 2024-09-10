class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #  中序非递归的思路：先一直压入左子树，直到左子树为空，然后弹出栈顶元素，再把右子树的左子树压入栈中，再把右子树压入栈中
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                cur = temp.right
        return res
