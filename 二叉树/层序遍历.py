from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        res = []
        q.append(root)
        while q:
            temp_list = []
            for _ in range(len(q)):
                temp = q.pop()
                temp_list.append(temp.val)
                if temp.left:
                    q.appendleft(temp.left)
                if temp.right:
                    q.appendleft(temp.right)
            res.append(temp_list)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    print(Solution().levelOrder(root))
