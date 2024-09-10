class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        low, fast = head, head.next
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        mid = low.next
        low.next = None  # 将链表分成两部分
        L = self.sortList(head)
        R = self.sortList(mid)
        h = res = ListNode(0)    
        # 合并
        while L and R:
            if L.val < R.val:
                h.next = L
                L = L.next
            else:
                h.next = R
                R = R.next
            h = h.next
        h.next = L if L else R
        return res.next
