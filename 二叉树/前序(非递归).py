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
        #  前序非递归的思路：先把根节点放入栈中，然后弹出栈顶元素，再把右子树放入栈中，再把左子树放入栈中
        stack = []
        if root:
            stack.append(root)
            res = []
            while stack:
                temp = stack.pop()
                res.append(temp.val)
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    stack.append(temp.left)
            return res
        else:
            return []


if __name__ == '__main__':
    root = TreeNode(5, TreeNode(4), TreeNode(6))
    node_1 = TreeNode(4, TreeNode(1), TreeNode(2))
    node_2 = TreeNode(6)
    node_3 = TreeNode(1)
    node_4 = TreeNode(2)
    root.left = node_1
    root.right = node_2
    node_1.left = node_3
    node_1.right = node_4
    print(Solution().preorderTraversal(root))
