# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def traversal(self, root, path, result):
        path.append(root.val)
        if not root.left and not root.right:
            str_route = '->'.join(map(str, path))  # 将path中的元素均变为str
            result.append(str_route)
        if root.left:
            self.traversal(root.left, path, result)
            path.pop()
        if root.right:
            self.traversal(root.right, path, result)
            path.pop()   # 这里的pop()是为了回溯，因为path是全局变量，所以需要回溯到上一层
        return result

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        return self.traversal(root, path=[], result=[])
