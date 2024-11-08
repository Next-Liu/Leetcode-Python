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
        dummyNode = ListNode(0, head)
        dummyNode.next.next = None
        p = head.next
        while p:
            q = p.next
            p.next = dummyNode.next
            dummyNode.next = p
            p = q
        return dummyNode.next
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
