class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #  原地逆置，头插法
        if head is None:
            return head
        pre = ListNode(0, head)
        p = head.next
        pre.next.next = None  # 重要，否则会成环
        while p:
            s = p.next
            p.next = pre.next
            pre.next = p
            p = s
        return pre.next
