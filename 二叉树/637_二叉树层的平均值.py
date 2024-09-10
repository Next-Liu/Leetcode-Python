from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype:List[float]
        """
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            sum = 0
            len_q = len(q)
            for _ in range(len_q):
                temp = q.pop()
                sum += temp.val
                if temp.right:
                    q.appendleft(temp.right)
                if temp.left:
                    q.appendleft(temp.left)
            res.append(float(sum/len_q))
        return res
