from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 当遍历到左右节点都为空的时候才到最低结点
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                temp = q.pop()
                if not temp.left and not temp.right:  # 当遍历到左右节点都为空的时候才到最低结点
                    return depth
                if temp.left:
                    q.appendleft(temp.left)
                if temp.right:
                    q.appendleft(temp.right)
