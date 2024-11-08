class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        dummy = ListNode(next=head)  # 头结点
        p0 = dummy
        while n >= k:
            n -= k
            pre = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next  # 保存下一个待反转部分的前一个节点
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next
