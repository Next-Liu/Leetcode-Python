# Definition for singly-linked list.
# 返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        low = fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if low == fast:  # 链表有环
                index1 = fast
                index2 = head
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        return None
