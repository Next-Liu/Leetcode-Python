class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n):
        dummy = ListNode(0, head)
        fast = dummy
        for _ in range(n):
            fast = fast.next
        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next