class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        cur = head
        while cur.next:
            p = cur.next
            if cur.val == p.val:
                cur.next = p.next
            else:
                cur = cur.next
        return head