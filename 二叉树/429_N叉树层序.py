from collections import deque


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root: Node):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        res.append([root.val])
        while q:
            temp_list = []
            for _ in range(len(q)):
                temp = q.pop()
                for child in temp.children:
                    temp_list.append(child.val)
                    q.appendleft(child)
            res.append(temp_list)
        res.pop()
        return res