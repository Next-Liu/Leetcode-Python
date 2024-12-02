class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        st = set(nums)
        dummy = ListNode(0,head)
        cur = dummy
        while cur.next:
            val = cur.next.val
            if val in st:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next