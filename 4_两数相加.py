# 给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0开头。
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = current = ListNode()  # 创建一个链表
        carry = 0  # 进位
        while l1 or l2 or carry:  # 防止最后carry还有进位，如999+9=1008
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            z = (x + y + carry) % 10  # 个位数
            carry = (x + y + carry) // 10  # 进位
            current.next = ListNode(z)  # 创建一个链表
            current = current.next  # 移动指针
            if l1: l1 = l1.next  # 移动指针
            if l2: l2 = l2.next  # 移动指针
        return result.next


if __name__ == '__main__':
    Node1 = ListNode(9)
    Node2 = ListNode(9)
    Node3 = ListNode(9)
    Node1.next = Node2
    Node2.next = Node3
    Node4 = ListNode(9)
    s = Solution.addTwoNumbers(Node1, Node4)
    while s:
        print(s.val, end=" ")
        s = s.next
