# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def traversal(self, inorder, postorder: list):
        if len(postorder) == 0:  #  如果是空的，那么返回None
            return None
        root = TreeNode(postorder[len(postorder) - 1])
        if len(postorder) == 1:
            return root
        index = 0
        while inorder[index] != postorder[len(postorder) - 1]:
            index += 1
        # 切分 inorder 和 postorder
        inorder_left = inorder[0:index]  # 左闭右开
        inorder_right = inorder[index + 1:len(inorder)]
        postorder.pop(len(postorder) - 1)
        postorder_left = postorder[0:index]
        postorder_right = postorder[index:len(postorder)]
        root.left = self.traversal(inorder_left, postorder_left)
        root.right = self.traversal(inorder_right, postorder_right)
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        res = self.traversal(inorder, postorder)
        return res
