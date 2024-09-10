from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 使用层序遍历，最后一层的第一个节点就是最左边的节点
        if not root:
            return 0
        q = deque()
        q.append(root)
        res = temp_list = []
        while q:
            for _ in range(len(q)):
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                temp_list.append(temp)
            res.append(temp_list)
            temp_list = []
        return res[len(res) - 1][0].val
